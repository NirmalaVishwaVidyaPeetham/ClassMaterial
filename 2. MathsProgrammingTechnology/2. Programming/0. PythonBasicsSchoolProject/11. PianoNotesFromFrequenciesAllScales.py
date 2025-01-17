import pyaudio
import numpy as np

def generate_note_frequencies():
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_frequencies = {}

    for octave in range(8):
        for note in note_names:
            key = f"{note}{octave}"
            frequency = 440 * 2 ** ((octave - 4) + (note_names.index(note) - 9) / 12)
            note_frequencies[key] = frequency

    return note_frequencies

note_frequencies = generate_note_frequencies()

def play_note(note, duration=0.5, sample_rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    fundamental = note_frequencies[note]
    harmonics = [fundamental * i for i in range(1, 6)]
    amplitudes = [1 / i for i in range(1, 6)]

    t = np.linspace(0, duration, int(sample_rate * duration), False)

    waveform = sum(amplitudes[i] * np.sin(2 * np.pi * harmonics[i] * t) for i in range(len(harmonics)))

    envelope = np.concatenate((np.linspace(0, 1, int(sample_rate * duration * 0.1)),
                               np.ones(int(sample_rate * duration * 0.8)),
                               np.linspace(1, 0, int(sample_rate * duration * 0.1))))
    waveform *= envelope

    stream.write(waveform.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

# Example usage
play_note('C3')  # Plays middle C
play_note('C4')
play_note('C5')
#play_note('E3')
#play_note('G3')