import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
import sounddevice as sd
from collections import deque
import time

"""
OVERALL SUMMARY:
This application is a high-precision, real-time 2D audio frequency monitor. 
It captures live microphone input and performs digital signal processing (DSP) 
to visualize the sound's spectral fingerprint. 

LAYOUT:
- LEFT COLUMN: Dynamic High-Resolution Pitch-Time Tracker (Full height).
  * Vertical Axis: Auto-adapts spontaneously when pitch exceeds current bounds.
  * Default Range: F2 to F4 (2 Octave span).
  * Gamaka Support: Low-latency smoothing allows tracking of rapid pitch ornaments.
- RIGHT TOP: Live Spectrum Analysis (50% of right column height).
- RIGHT BOTTOM: Text Box showing history of detected notes.
"""

# ================== SETTINGS ==================
SAMPLE_RATE = 44100
FFT_SIZE = 4096  # High resolution for precise note separation
CHANNELS = 1
DISPLAY_FMIN = 50
DISPLAY_FMAX = 2000
UPDATE_INTERVAL = 20  # 50 FPS

A4_FREQ = 440.0
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

NOTE_COLORS = {
    'C': '#FF0000', 'C#': '#222222', 'D': '#FF7F00', 'D#': '#222222',
    'E': '#FFFF00', 'F': '#00FF00', 'F#': '#222222', 'G': '#0000FF',
    'G#': '#222222', 'A': '#4B0082', 'A#': '#222222', 'B': '#8B00FF'
}

# Tempo Settings
BEAT_DURATION = 2.0
HISTORY_SECONDS = 15
MAX_SAMPLES = int(HISTORY_SECONDS / (UPDATE_INTERVAL / 1000.0))

# Dynamic Y-Axis State: Defaulting to F2 (41) to F4 (65)
current_y_min = 41
current_y_max = 65
Y_SPAN = 24  # 2 Octave span

# Buffers
note_history = deque(maxlen=3)
freq_history = deque(maxlen=2)

# --- GAMAKA OPTIMIZED SMOOTHING ---
# Stage 1: Median filter (removes jumps/outliers)
glissando_smooth_buffer = deque(maxlen=5)
# Stage 2: Exponential Moving Average (removes jitter/noise)
last_ema_midi = None
EMA_ALPHA = 0.6

# Buffers for Transcription History
transcription_notes = deque(maxlen=60)
beat_onsets = deque(maxlen=100)
pitch_path_buffer = deque(maxlen=MAX_SAMPLES)

start_time = time.time()
last_transcribed_note_in_beat = None
last_beat_index = -1
prev_rms = 0.0
melody_display_str = "| "


# ================== HELPERS ==================
def freq_to_note(f):
    if f < 20: return ""
    semitones = 12 * np.log2(f / A4_FREQ) + 69
    midi_note = int(np.round(semitones))
    note_idx = midi_note % 12
    octave = (midi_note // 12) - 1
    if octave < -1 or octave > 9: return ""
    return f"{NOTE_NAMES[note_idx]}{octave}"


def yin_pitch_detection(sig, sr, threshold=0.10):
    N = len(sig)
    tau_min = int(sr / 3000)
    tau_max = int(sr / 60)

    sig_sq = sig ** 2
    cum_sig_sq = np.insert(np.cumsum(sig_sq), 0, 0)

    n_fft = 2 ** int(np.ceil(np.log2(2 * N)))
    f_sig = np.fft.fft(sig, n=n_fft)
    acf = np.real(np.fft.ifft(f_sig * np.conj(f_sig)))

    diff = np.zeros(tau_max)
    for tau in range(1, tau_max):
        e1 = cum_sig_sq[N - tau]
        e2 = cum_sig_sq[N] - cum_sig_sq[tau]
        diff[tau] = e1 + e2 - 2 * acf[tau]

    cmndf = np.zeros(tau_max)
    cmndf[0] = 1
    running_sum = 0
    for tau in range(1, tau_max):
        running_sum += diff[tau]
        cmndf[tau] = diff[tau] / ((1 / tau) * running_sum + 1e-10)

    tau_found = -1
    for tau in range(tau_min, tau_max - 1):
        if cmndf[tau] < threshold:
            if cmndf[tau] < cmndf[tau - 1] and cmndf[tau] < cmndf[tau + 1]:
                tau_found = tau
                break

    if tau_found == -1:
        tau_found = np.argmin(cmndf[tau_min:tau_max]) + tau_min

    rms = np.sqrt(np.mean(sig ** 2))
    if rms < 0.005 or cmndf[int(tau_found)] > 0.35:
        return None, rms

    # Parabolic Interpolation for sub-Hz accuracy
    if 0 < tau_found < tau_max - 1:
        idx = int(tau_found)
        y1, y2, y3 = cmndf[idx - 1], cmndf[idx], cmndf[idx + 1]
        denom = y1 - 2 * y2 + y3
        if abs(denom) > 1e-10:
            offset = 0.5 * (y1 - y3) / denom
            tau_found += offset

    return sr / tau_found, rms


# ================== PLOT SETUP ==================
plt.style.use('dark_background')
fig = plt.figure(figsize=(15, 9))

# GS structure: Left column Timeline, Right split into Spectrum and Text
gs = fig.add_gridspec(2, 2, width_ratios=[1.5, 1.0], height_ratios=[1.0, 1.0])
fig.subplots_adjust(left=0.06, right=0.96, bottom=0.1, top=0.9, wspace=0.35, hspace=0.4)

# --- LEFT COLUMN: Timeline (gs[:, 0]) ---
ax_hist = fig.add_subplot(gs[:, 0])
ax_hist.set_xlim(-HISTORY_SECONDS, 0)
ax_hist.set_ylim(current_y_min - 0.5, current_y_max + 0.5)
ax_hist.set_title("Precision Transcription Timeline (F2 - F4)")
ax_hist.set_xlabel("Time (Seconds ago)")
ax_hist.set_ylabel("Musical Note")

grid_lines = []


def update_piano_grid(y_min, y_max):
    global grid_lines
    for gl_item in grid_lines: gl_item.remove()
    grid_lines = []
    yticks, ylabels = [], []
    for m in range(int(y_min) - 1, int(y_max) + 2):
        name_full = freq_to_note(A4_FREQ * (2 ** ((m - 69) / 12.0)))
        if not name_full: continue
        base = name_full.strip('0123456789-')
        c = NOTE_COLORS.get(base, '#222222')
        alpha = 0.3 if '#' not in name_full else 0.1
        gl = ax_hist.axhline(m, color=c, alpha=alpha, lw=1.2, zorder=0)
        grid_lines.append(gl)
        if '#' not in name_full:
            yticks.append(m);
            ylabels.append(name_full)
    ax_hist.set_yticks(yticks)
    ax_hist.set_yticklabels(ylabels, fontsize=8)


update_piano_grid(current_y_min, current_y_max)
pitch_path_line, = ax_hist.plot([], [], color='#00FF00', lw=2.5, alpha=1.0, zorder=10)
beat_lines = [ax_hist.axvline(-100, color='red', alpha=0.4, linestyle='-', lw=1.5, zorder=5) for _ in range(100)]

# --- RIGHT TOP: Spectrum (gs[0, 1]) ---
ax = fig.add_subplot(gs[0, 1])
freqs_all = np.fft.rfftfreq(FFT_SIZE, 1.0 / SAMPLE_RATE)
mask = (freqs_all >= DISPLAY_FMIN) & (freqs_all <= DISPLAY_FMAX)
freqs_plot = freqs_all[mask]
line, = ax.plot(freqs_plot, np.full_like(freqs_plot, -100), color='#00FFCC', lw=1.2, alpha=0.8)
fill = ax.fill_between(freqs_plot, -100, -100, color='#00FFCC', alpha=0.15)
peak_vline = ax.axvline(0, color='#00FF00', linestyle='--', alpha=0, lw=1.5)
peak_text = ax.text(0.05, 0.85, '', transform=ax.transAxes, color='#00FF00', fontweight='bold', fontsize=11,
                    bbox=dict(facecolor='black', alpha=0.8, edgecolor='#00FF00'))
secondary_labels = [ax.text(0, 0, '', color='#FF4444', fontsize=9, fontweight='bold') for _ in range(12)]
ax.set_xscale('log')
ax.set_xlim(DISPLAY_FMIN, DISPLAY_FMAX)
ax.set_ylim(-80, 0)
ax.set_title("Live Spectrum Analysis")
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x)}" if x >= 1000 else f"{x:.0f}"))

# --- RIGHT BOTTOM: Text Box (gs[1, 1]) ---
ax_text = fig.add_subplot(gs[1, 1])
ax_text.set_axis_off()
ax_text.set_title("Transcription History", color='white', pad=10)
melody_text_box = ax_text.text(0.02, 0.95, "Notes detected: | ", color='#00FFCC',
                               fontsize=10, va='top', ha='left', wrap=True, family='monospace',
                               transform=ax_text.transAxes)

# ================== MAIN LOOP ==================
audio_buffer = np.zeros(FFT_SIZE, dtype=np.float32)


def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = np.roll(audio_buffer, -frames)
    audio_buffer[-frames:] = indata.ravel()


def update(frame):
    global fill, last_transcribed_note_in_beat, prev_rms, last_beat_index, melody_display_str
    global current_y_min, current_y_max, last_ema_midi
    chunk = audio_buffer.copy()
    now_abs = time.time() - start_time

    # FFT
    window = np.blackman(FFT_SIZE)
    fft_res = np.abs(np.fft.rfft(chunk * window)) / (FFT_SIZE / 2.0)
    mag_db = 20 * np.log10(fft_res + 1e-8)
    line.set_ydata(mag_db[mask])
    if fill: fill.remove()
    fill = ax.fill_between(freqs_plot, -80, mag_db[mask], color='#00FFCC', alpha=0.1)

    # Pitch & Metronome Sync
    raw_freq, rms_vol = yin_pitch_detection(chunk, SAMPLE_RATE, threshold=0.10)
    current_beat_idx = int(now_abs / BEAT_DURATION)
    if current_beat_idx > last_beat_index:
        last_beat_index = current_beat_idx
        beat_onsets.append(now_abs)
        last_transcribed_note_in_beat = None
        melody_display_str += "| "
        print("| ", end='', flush=True)

    if raw_freq:
        # --- ENHANCED GAMAKA SMOOTHING ---
        midi_val_raw = 12 * np.log2(raw_freq / A4_FREQ) + 69
        glissando_smooth_buffer.append(midi_val_raw)
        midi_median = np.median(glissando_smooth_buffer)

        if last_ema_midi is None:
            last_ema_midi = midi_median
        else:
            last_ema_midi = EMA_ALPHA * midi_median + (1.0 - EMA_ALPHA) * last_ema_midi

        pitch_path_buffer.append((now_abs, last_ema_midi))

        # --- SPONTANEOUS AXIS LOGIC ---
        if last_ema_midi > current_y_max:
            current_y_min += 12;
            current_y_max += 12
            ax_hist.set_ylim(current_y_min - 0.5, current_y_max + 0.5)
            update_piano_grid(current_y_min, current_y_max)
        elif last_ema_midi < current_y_min and current_y_min > 12:
            current_y_min -= 12;
            current_y_max -= 12
            ax_hist.set_ylim(current_y_min - 0.5, current_y_max + 0.5)
            update_piano_grid(current_y_min, current_y_max)

        note = freq_to_note(raw_freq)
        note_history.append(note)
        stable_note = max(set(note_history), key=note_history.count)

        # Update Tracker UI
        peak_vline.set_xdata([raw_freq]);
        peak_vline.set_alpha(0.8)
        peak_text.set_text(f"  {stable_note}  \n  {raw_freq:.1f} Hz  ")

        if stable_note != last_transcribed_note_in_beat and rms_vol > 0.01:
            transcription_notes.append((stable_note, now_abs))
            last_transcribed_note_in_beat = stable_note
            melody_display_str += f"{stable_note} "
            print(f"{stable_note} ", end='', flush=True)

        # Harmonics
        mag_plot = mag_db[mask]
        other_peaks = []
        for i in range(1, len(mag_plot) - 1):
            if mag_plot[i] > mag_plot[i - 1] and mag_plot[i] > mag_plot[i + 1]:
                if mag_db[i] > (mag_db.max() - 25) and abs(freqs_plot[i] - raw_freq) > (raw_freq * 0.1):
                    other_peaks.append((freqs_plot[i], mag_db[i]))
        other_peaks.sort(key=lambda x: x[1], reverse=True)
        for i, label in enumerate(secondary_labels):
            if i < len(other_peaks):
                f_o, m_o = other_peaks[i]
                label.set_text(freq_to_note(f_o));
                label.set_position((f_o, m_o + 2));
                label.set_visible(True)
            else:
                label.set_visible(False)
    else:
        last_ema_midi = None
        pitch_path_buffer.append((now_abs, np.nan))
        peak_vline.set_alpha(0);
        peak_text.set_text("")
        for label in secondary_labels: label.set_visible(False)
        last_transcribed_note_in_beat = None

    # Update Text Box UI
    display_limit = 350
    txt = melody_display_str if len(melody_display_str) <= display_limit else "..." + melody_display_str[
                                                                                      -display_limit:]
    melody_text_box.set_text(f"Notes detected:\n{txt}")

    # Render Timeline
    if len(pitch_path_buffer) > 1:
        path_data = np.array(pitch_path_buffer)
        pitch_path_line.set_data(path_data[:, 0] - now_abs, path_data[:, 1])

    for i, b_line in enumerate(beat_lines):
        if i < len(beat_onsets):
            rel_t = beat_onsets[i] - now_abs
            if rel_t > -HISTORY_SECONDS:
                b_line.set_xdata([rel_t]);
                b_line.set_alpha(max(0, 0.4 + (rel_t / (HISTORY_SECONDS * 1.5))));
                b_line.set_visible(True)
            else:
                b_line.set_visible(False)
        else:
            b_line.set_visible(False)


# ================== START ==================
stream = sd.InputStream(samplerate=SAMPLE_RATE, blocksize=FFT_SIZE // 16, channels=CHANNELS, callback=audio_callback,
                        latency='low')
ani = FuncAnimation(fig, update, interval=UPDATE_INTERVAL, blit=False, cache_frame_data=False)
with stream:
    print("Gamaka-Optimized Transcription Active. Tempo: 30 BPM.");
    plt.show()