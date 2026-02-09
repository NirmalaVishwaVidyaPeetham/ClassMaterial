import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
import sounddevice as sd
from collections import deque

"""
OVERALL SUMMARY:
This application is a high-precision, real-time 2D audio frequency monitor. 
It captures live microphone input and performs digital signal processing (DSP) 
to visualize the sound's spectral fingerprint. By combining Fast Fourier 
Transform (FFT) for broad harmonic analysis and the YIN algorithm for 
accurate fundamental pitch detection, the tool provides immediate visual 
feedback on musical notes. It is optimized for piano and vocal use, 
displaying the primary pitch in green and overtones in red to aid in 
technical training and resonance analysis.
"""

"""
VOCAL TRAINING GUIDE:
1. FUNDAMENTAL STABILITY (Green Tracker):
   - Aim for a rock-steady green line. If it flickers or jumps, your vocal cord closure 
     is likely inconsistent. Practice "gentle onsets" to lock the pitch early.
2. RESONANCE & HARMONICS (Red Labels):
   - CHEST VOICE (Lows): Look for tall Red labels close to the Green tracker.
   - HEAD VOICE (Highs): Space between Red labels widens. Focus on keeping the 2nd 
     and 3rd Red labels prominent to maintain "ring" and avoid a thin sound.
3. VOWEL MODIFICATION:
   - If high notes feel difficult, slightly shift your vowel (e.g., 'Ooh' towards 'Ah').
   - Watch the Red labels; when they "boost" in height during a shift, you've found 
     vocal tract resonance (formant tuning), making the note feel effortless.
4. DETECTING STRAIN (Cyan Valleys):
   - High-quality notes have deep, clean "valleys" between the peaks.
   - If the Cyan area looks "fuzzy" or jagged between peaks, you are likely pushing 
     too much air or experiencing throat tension. Aim for a clean, sharp spectrum.

CODE EXECUTION FLOW:
1. CAPTURE: 'sounddevice' captures raw audio from the mic in the background.
2. CALLBACK: 'audio_callback' continuously pushes new audio into a rolling 'audio_buffer'.
3. ANALYSIS (Every 30ms):
    a. FFT: Converts the time-domain buffer into the frequency-domain (Spectrum).
    b. MAGNITUDE: Calculates Decibels (dB) to show volume relative to a reference.
    c. YIN: A specialized algorithm finds the "Fundamental" (Main Note).
4. RENDERING:
    a. The main note is drawn in GREEN with a dashed vertical tracker.
    b. Secondary peaks (harmonics) are identified and labeled in RED.
    c. The full spectrum is plotted with a cyan fill.
"""

# ================== SETTINGS ==================
SAMPLE_RATE = 44100
FFT_SIZE = 16384  # High resolution for precise note separation
CHANNELS = 1
DISPLAY_FMIN = 50
DISPLAY_FMAX = 2000
UPDATE_INTERVAL = 30

A4_FREQ = 440.0
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Temporal smoothing buffers to prevent UI flickering
note_history = deque(maxlen=6)
freq_history = deque(maxlen=4)


# ================== HELPERS ==================
def freq_to_note(f):
    """Converts a raw frequency (Hz) to a standard MIDI note name (e.g. C4)."""
    if f < 20: return ""
    # MIDI formula: 12 * log2(f/440) + 69
    semitones = 12 * np.log2(f / A4_FREQ) + 69
    midi_note = int(np.round(semitones))
    note_idx = midi_note % 12
    octave = (midi_note // 12) - 1
    if octave < 0 or octave > 9: return ""
    return f"{NOTE_NAMES[note_idx]}{octave}"


def yin_pitch_detection(sig, sr, threshold=0.15):
    """
    ALGORITHM: YIN PITCH DETECTION

    1. DIFFERENCE FUNCTION: Compares the signal to a delayed version of itself.
    2. CMNDF: Normalizes the difference to avoid 'octave errors' where the
       algorithm might mistake an overtone for the fundamental note.
    3. SEARCH: Finds the first significant 'dip' below the threshold (0.15).
       This dip represents the most likely fundamental frequency.
    4. INTERPOLATION: Uses parabolic math to find the peak center between bins,
       allowing for 0.1 Hz precision even with standard sample rates.
    """
    N = len(sig)
    # Target search range: A0 (27.5Hz) to C8 (4186Hz)
    tau_min = int(sr / 4500)
    tau_max = int(sr / 25)

    # Vectorized Difference Function
    diff = np.zeros(tau_max)
    for tau in range(1, tau_max):
        delta = sig[:N - tau] - sig[tau:]
        diff[tau] = np.sum(delta ** 2)

    # Cumulative Mean Normalized Difference Function
    cmndf = np.zeros(tau_max)
    cmndf[0] = 1
    running_sum = 0
    for tau in range(1, tau_max):
        running_sum += diff[tau]
        cmndf[tau] = diff[tau] / ((1 / tau) * running_sum + 1e-10)

    # Look for first local minimum below threshold
    tau_found = -1
    for tau in range(tau_min, tau_max - 1):
        if cmndf[tau] < threshold:
            if cmndf[tau] < cmndf[tau - 1] and cmndf[tau] < cmndf[tau + 1]:
                tau_found = tau
                break

    if tau_found == -1:
        tau_found = np.argmin(cmndf[tau_min:tau_max]) + tau_min

    rms = np.sqrt(np.mean(sig ** 2))
    # Threshold check: ensures signal isn't just room noise
    if rms < 0.005 or cmndf[int(tau_found)] > 0.4:
        return None, -100

    # Parabolic Interpolation for sub-sample accuracy
    if 0 < tau_found < tau_max - 1:
        idx = int(tau_found)
        y1, y2, y3 = cmndf[idx - 1], cmndf[idx], cmndf[idx + 1]
        denom = y1 - 2 * y2 + y3
        if abs(denom) > 1e-10:
            offset = 0.5 * (y1 - y3) / denom
            tau_found += offset

    return sr / tau_found, rms


# Precompute visible note positions for the top axis grid
note_freqs = []
note_labels = []
for midi in range(21, 108):
    f = A4_FREQ * (2 ** ((midi - 69) / 12.0))
    if DISPLAY_FMIN <= f <= DISPLAY_FMAX:
        note_freqs.append(f)
        label = freq_to_note(f)
        # Show labels for C, E, G, and A4 to keep UI clean
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

# Main Pitch Tracker (GREEN)
peak_vline = ax.axvline(0, color='#00FF00', linestyle='--', alpha=0, lw=1.5)
peak_text = ax.text(0, 0, '', color='#00FF00', fontweight='bold', fontsize=12,
                    bbox=dict(facecolor='black', alpha=0.8, edgecolor='#00FF00'))

# Secondary Note Labels (RED) - Initializing a larger pool of 12 labels
secondary_labels = [ax.text(0, 0, '', color='#FF4444', fontsize=9, fontweight='bold') for _ in range(12)]

ax.set_xscale('log')
ax.set_xlim(DISPLAY_FMIN, DISPLAY_FMAX)
ax.set_ylim(-80, 0)

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title("YIN Spectrum Monitor: Green (Main) & Red (Overtones)")

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
    """Captures audio chunks and slides them into the rolling buffer."""
    global audio_buffer
    audio_buffer = np.roll(audio_buffer, -frames)
    audio_buffer[-frames:] = indata[:, 0] if indata.ndim > 1 else indata.ravel()


# ================== ANIMATION UPDATE ==================
def update(frame):
    """Main loop: Performs FFT, YIN detection, and updates the plot UI."""
    global fill
    chunk = audio_buffer.copy()

    # FFT for visual spectrum display
    window = np.blackman(FFT_SIZE)
    fft_vals = np.fft.rfft(chunk * window)
    mag_linear = np.abs(fft_vals) / (FFT_SIZE / 2.0)
    mag_db = 20 * np.log10(mag_linear + 1e-8)
    mag_plot = mag_db[mask]

    # Update spectrum line and area fill
    line.set_ydata(mag_plot)
    fill.remove()
    fill = ax.fill_between(freqs_plot, -80, mag_plot, color='#00FFCC', alpha=0.1)

    # Use YIN for main pitch detection
    raw_freq, rms_volume = yin_pitch_detection(chunk, SAMPLE_RATE, threshold=0.15)

    if raw_freq:
        freq_history.append(raw_freq)
        avg_freq = np.mean(freq_history)

        note = freq_to_note(avg_freq)
        note_history.append(note)
        stable_note = max(set(note_history), key=note_history.count)

        # Update Main Note Tracker (GREEN)
        peak_vline.set_xdata([avg_freq])
        peak_vline.set_alpha(0.8)
        peak_text.set_position((avg_freq, -25))
        peak_text.set_text(f"  {stable_note}  \n  {avg_freq:.1f} Hz  ")

        # --- SECONDARY NOTE DETECTION (RED) ---
        # Look for other prominent peaks in the magnitude spectrum
        other_peaks = []
        for i in range(1, len(mag_plot) - 1):
            if mag_plot[i] > mag_plot[i - 1] and mag_plot[i] > mag_plot[i + 1]:
                # Peak must be within 30dB of the max (more generous) and not the fundamental note
                if mag_plot[i] > (mag_plot.max() - 30) and abs(freqs_plot[i] - avg_freq) > (avg_freq * 0.1):
                    other_peaks.append((freqs_plot[i], mag_plot[i]))

        other_peaks.sort(key=lambda x: x[1], reverse=True)

        # Display secondary notes in RED
        for i, label in enumerate(secondary_labels):
            if i < len(other_peaks):
                f_other, m_other = other_peaks[i]
                n_other = freq_to_note(f_other)
                label.set_text(n_other)
                label.set_position((f_other, m_other + 2))
                label.set_alpha(1)
            else:
                label.set_alpha(0)
    else:
        # Hide trackers if silence
        peak_vline.set_alpha(0)
        peak_text.set_text("")
        for label in secondary_labels: label.set_alpha(0)

    return [line, fill, peak_vline, peak_text] + secondary_labels


# ================== START ==================
stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=FFT_SIZE // 16,
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
    print("YIN Engine active. Tracking main note (Green) and overtones (Red).")
    plt.show()