import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
import sounddevice as sd
from collections import deque

# ================== SETTINGS ==================
SAMPLE_RATE = 44100
FFT_SIZE = 16384  # Optimized for YIN (balance between latency and precision)
CHANNELS = 1
DISPLAY_FMIN = 50
DISPLAY_FMAX = 2000
UPDATE_INTERVAL = 30

A4_FREQ = 440.0
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Temporal smoothing to prevent flickering (Vocal Pitch Monitor style)
note_history = deque(maxlen=6)
freq_history = deque(maxlen=4)


# ================== HELPERS ==================
def freq_to_note(f):
    if f < 20: return ""
    semitones = 12 * np.log2(f / A4_FREQ) + 69
    midi_note = int(np.round(semitones))
    note_idx = midi_note % 12
    octave = (midi_note // 12) - 1
    if octave < 0 or octave > 9: return ""
    return f"{NOTE_NAMES[note_idx]}{octave}"


def yin_pitch_detection(sig, sr, threshold=0.15):
    """
    Implements a robust version of the YIN algorithm.
    1. Difference Function
    2. Cumulative Mean Normalized Difference Function (CMNDF)
    3. Absolute Thresholding
    """
    N = len(sig)
    # Search range for piano frequencies (27.5Hz to ~4000Hz)
    tau_min = int(sr / 4500)
    tau_max = int(sr / 25)

    # 1. Difference Function
    # We use a vectorized approach for speed
    diff = np.zeros(tau_max)
    for tau in range(1, tau_max):
        # Calculate sum of squared differences
        delta = sig[:N - tau] - sig[tau:]
        diff[tau] = np.sum(delta ** 2)

    # 2. Cumulative Mean Normalized Difference Function (CMNDF)
    cmndf = np.zeros(tau_max)
    cmndf[0] = 1
    running_sum = 0
    for tau in range(1, tau_max):
        running_sum += diff[tau]
        cmndf[tau] = diff[tau] / ((1 / tau) * running_sum)

    # 3. Find the first local minimum below the threshold
    tau_found = -1
    for tau in range(tau_min, tau_max - 1):
        if cmndf[tau] < threshold:
            # Check if it's a local minimum
            if cmndf[tau] < cmndf[tau - 1] and cmndf[tau] < cmndf[tau + 1]:
                tau_found = tau
                break

    # If no minimum below threshold, use the global minimum in range
    if tau_found == -1:
        tau_found = np.argmin(cmndf[tau_min:tau_max]) + tau_min

    # Check if the signal is loud enough to be valid
    rms = np.sqrt(np.mean(sig ** 2))
    if rms < 0.005 or cmndf[tau_found] > 0.4:  # Signal is too noisy or quiet
        return None, -100

    # 4. Parabolic Interpolation for sub-bin precision
    if 0 < tau_found < tau_max - 1:
        y1, y2, y3 = cmndf[tau_found - 1], cmndf[tau_found], cmndf[tau_found + 1]
        denom = y1 - 2 * y2 + y3
        if abs(denom) > 1e-10:
            offset = 0.5 * (y1 - y3) / denom
            tau_found += offset

    return sr / tau_found, rms


# Precompute visible note positions & labels
note_freqs = []
note_labels = []
for midi in range(21, 108):
    f = A4_FREQ * (2 ** ((midi - 69) / 12.0))
    if DISPLAY_FMIN <= f <= DISPLAY_FMAX:
        note_freqs.append(f)
        label = freq_to_note(f)
        if any(n in label for n in ['C', 'E', 'G']) or 'A4' in label:
            note_labels.append(label)
        else:
            note_labels.append("")

# ================== DATA ARRAYS ==================
freqs_all = np.fft.rfftfreq(FFT_SIZE, 1.0 / SAMPLE_RATE)
mask = (freqs_all >= DISPLAY_FMIN) & (freqs_all <= DISPLAY_FMAX)
freqs_plot = freqs_all[mask]

# ================== PLOT SETUP ==================
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))
fig.subplots_adjust(left=0.08, right=0.95, bottom=0.15, top=0.85)

line, = ax.plot(freqs_plot, np.full_like(freqs_plot, -100), color='#00FFCC', lw=1.2, alpha=0.8)
fill = ax.fill_between(freqs_plot, -100, -100, color='#00FFCC', alpha=0.15)

peak_vline = ax.axvline(0, color='yellow', linestyle='--', alpha=0, lw=1.5)
peak_text = ax.text(0, 0, '', color='yellow', fontweight='bold', fontsize=12,
                    bbox=dict(facecolor='black', alpha=0.8, edgecolor='#00FFCC'))

ax.set_xscale('log')
ax.set_xlim(DISPLAY_FMIN, DISPLAY_FMAX)
ax.set_ylim(-80, 0)

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title("YIN-Algorithm Piano Monitor: High Precision Tracking")

ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x)}" if x >= 1000 else f"{x:.0f}"))

ax_notes = ax.twiny()
ax_notes.set_xscale('log')
ax_notes.set_xlim(ax.get_xlim())
ax_notes.set_xticks(note_freqs)
ax_notes.set_xticklabels(note_labels, fontsize=8)

for nf in note_freqs:
    ax.axvline(nf, color='white', alpha=0.08, lw=0.5)

# ================== AUDIO BUFFER ==================
audio_buffer = np.zeros(FFT_SIZE, dtype=np.float32)


def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = np.roll(audio_buffer, -frames)
    audio_buffer[-frames:] = indata[:, 0] if indata.ndim > 1 else indata.ravel()


# ================== ANIMATION UPDATE ==================
def update(frame):
    global fill
    chunk = audio_buffer.copy()

    # Visual Spectrum update (Keeping it for visual context)
    window = np.blackman(FFT_SIZE)
    fft_vals = np.fft.rfft(chunk * window)
    mag_linear = np.abs(fft_vals) / (FFT_SIZE / 2.0)
    mag_db = 20 * np.log10(mag_linear + 1e-8)
    mag_plot = mag_db[mask]

    line.set_ydata(mag_plot)
    fill.remove()
    fill = ax.fill_between(freqs_plot, -80, mag_plot, color='#00FFCC', alpha=0.1)

    # Use YIN Algorithm for professional-grade pitch detection
    # Threshold 0.15 is the standard for musical pitch tracking
    raw_freq, rms_volume = yin_pitch_detection(chunk, SAMPLE_RATE, threshold=0.15)

    if raw_freq:
        freq_history.append(raw_freq)
        avg_freq = np.mean(freq_history)

        note = freq_to_note(avg_freq)
        note_history.append(note)

        # Stability check
        stable_note = max(set(note_history), key=note_history.count)

        # Get visual height for text placement (find closest bin in plot)
        peak_mag_db = -25  # Default height for label

        peak_vline.set_xdata([avg_freq])
        peak_vline.set_alpha(0.8)
        peak_text.set_position((avg_freq, peak_mag_db))
        peak_text.set_text(f"  {stable_note}  \n  {avg_freq:.1f} Hz  ")
    else:
        peak_vline.set_alpha(0)
        peak_text.set_text("")

    return line, fill, peak_vline, peak_text


# ================== START ==================
stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=FFT_SIZE // 16,  # High resolution update
    channels=CHANNELS,
    callback=audio_callback,
    latency='low'
)

ani = FuncAnimation(
    fig, update,
    interval=UPDATE_INTERVAL,
    blit=True,
    cache_frame_data=False
)

with stream:
    print("YIN Engine active. Tracking piano pitch with high stability.")
    plt.show()