import pyaudio
import numpy as np

note_frequencies = {
    'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81,
    'F3': 174.61, 'F#3': 185, 'G3': 196, 'G#3': 207.35, 'A3': 220,
    'A#3': 233.08, 'B3': 246.94,
}


def play_note(note, duration=0.5):
    p = pyaudio.PyAudio()

    # Use a standard sample rate (e.g., 44100 Hz)
    sample_rate = 44100

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Generate sine wave samples
    samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * note_frequencies[note] / sample_rate)).astype(
        np.float32)

    # Play the samples
    stream.write(samples.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()


# Now you can call the function as before:
for i in range(10):
    play_note('C3')
    play_note('C#3')
    #play_note('D3')