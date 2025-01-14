import pygame.midi

def play_piano_notes(notes, tempo=120):
    """
    Plays a sequence of piano notes using Pygame MIDI.

    Args:
        notes: A list of tuples, where each tuple contains the note (MIDI number) and duration (in beats).
        tempo: The tempo of the music in beats per minute (default 120).
    """

    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)  # Piano instrument

    for note, duration in notes:
        player.note_on(note, 127)  # Note on (full velocity)
        pygame.time.delay(int(60 / tempo * duration * 1000))  # Delay for note duration
        player.note_off(note, 127)  # Note off

    del player
    pygame.midi.quit()


# Example usage:
# notes = [(60, 1), (64, 1), (67, 1), (64, 1)]  # C major chord
# play_piano_notes(notes)

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

# Example usage:
# print(note_to_midi("C4"))  # Output: 60
# print(note_to_midi("C#4")) # Output: 61
# print(note_to_midi("Db4")) # Output: 61
# print(type(notes))

play_piano_notes([(note_to_midi("C4"),2)])

def ourNotePlayingFunction(ourSongNotes):
    notes = []
    for ourSongNote in ourSongNotes:
        notes.append((note_to_midi(ourSongNote), 1))
    print(notes)
    play_piano_notes(notes)

ourSongNotes = ["E3", "E3", "G3","G3","G3", "G3", "A3", "G3", "C4", "C4", "C4", "C4"]
ourNotePlayingFunction(ourSongNotes)

