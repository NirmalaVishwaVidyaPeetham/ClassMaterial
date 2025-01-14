import simpleaudio as sa
        ## https://pypi.org/project/simpleaudio-patched/ Install this patched version to get it working with Python3.12
import numpy as np

# Define the frequencies of the notes with both sharp and flat names
notes = {
    "C2": 65.41, "C#2": 69.30, "Db2": 69.30, "D2": 73.42, "D#2": 77.78, "Eb2": 77.78, "E2": 82.41, "F2": 87.31, "F#2": 92.50, "Gb2": 92.50, "G2": 98.00, "G#2": 103.83, "Ab2": 103.83, "A2": 110.00, "A#2": 116.54, "Bb2": 116.54, "B2": 123.47,
    "C3": 130.81, "C#3": 138.59, "Db3": 138.59, "D3": 146.83, "D#3": 155.56, "Eb3": 155.56, "E3": 164.81, "F3": 174.61, "F#3": 185.00, "Gb3": 185.00, "G3": 196.00, "G#3": 207.65, "Ab3": 207.65, "A3": 220.00, "A#3": 233.08, "Bb3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4": 277.18, "Db4": 277.18, "D4": 293.66, "D#4": 311.13, "Eb4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99, "Gb4": 369.99, "G4": 392.00, "G#4": 415.30, "Ab4": 415.30, "A4": 440.00, "A#4": 466.16, "Bb4": 466.16, "B4": 493.88,
    "C5": 523.25, "C#5": 554.37, "Db5": 554.37, "D5": 587.33, "D#5": 622.25, "Eb5": 622.25, "E5": 659.25, "F5": 698.46, "F#5": 739.99, "Gb5": 739.99, "G5": 783.99, "G#5": 830.61, "Ab5": 830.61, "A5": 880.00, "A#5": 932.33, "Bb5": 932.33, "B5": 987.77
    # Add more notes as needed
}

def play_note(note, duration=1, sample_rate=44100):
    """Plays a musical note with a harmonium-like timbre.

    Args:
      note: The musical note to play (e.g., "C4", "D#2", "Eb4").
      duration: The duration of the note in seconds.
      sample_rate: The sample rate in Hz.
    """
    if note in notes:
        frequency = notes[note]
        t = np.linspace(0, duration, int(sample_rate * duration), False)

        # Combine harmonics with adjusted amplitudes for harmonium-like sound
        audio = (
            np.sin(frequency * t * 2 * np.pi) * 0.7 +  # Fundamental frequency
            np.sin(2 * frequency * t * 2 * np.pi) * 0.4 +  # 2nd harmonic
            np.sin(3 * frequency * t * 2 * np.pi) * 0.2 +  # 3rd harmonic
            np.sin(4 * frequency * t * 2 * np.pi) * 0.1   # 4th harmonic
        )

        # Apply a slightly slower decay envelope
        decay_rate = 0.003  # Adjust for faster/slower decay
        envelope = np.exp(-decay_rate * t)
        audio *= envelope

        # Add a slight vibrato effect
        vibrato_frequency = 5  # Hz
        vibrato_depth = 0.005
        audio *= 1 + vibrato_depth * np.sin(2 * np.pi * vibrato_frequency * t)

        # Normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        # Start playback
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()
    else:
        print(f"Note {note} not found.")

def play_piano_notes(notes, tempo=120):
    """
    Plays a sequence of piano notes using simpleaudio.

    Args:
        notes: A list of tuples, where each tuple contains the note (string, e.g., "C4") and duration (in beats).
        tempo: The tempo of the music in beats per minute (default 120).
    """
    for note, duration in notes:
        play_note(note, duration=60/tempo * duration)


def note_to_midi(note):
  """
  Converts a piano note (e.g., C3#, D4b) to its corresponding MIDI number.

  Args:
    note: A string representing the piano note (e.g., "C4", "C#4", "Db4").

  Returns:
    The MIDI number of the note, or None if the note is invalid.
  """
  note_map = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
  try:
    note_name, octave = note[:-1], int(note[-1])
    note_value = note_map[note_name]
    midi_number = 12 * (octave + 1) + note_value  # MIDI numbers start at C0 = 12
    return midi_number
  except (KeyError, ValueError):
    print(f"Invalid note: {note}")
    return None


def ourNotePlayingFunction(ourSongNotes):
    notes = []
    for ourSongNote in ourSongNotes:
        notes.append((ourSongNote, 1))  # Use note string directly
    print(notes)
    play_piano_notes(notes)

# Example usage:
# ourSongNotes = ["E3", "E3", "G3","G3","G3", "G3", "A3", "G3", "C4", "C4", "C4", "C4"]
# ourNotePlayingFunction(ourSongNotes)