from OurLibraryOfFunctions.PlayPianoNotes_SimpleAudio import *

Song1Notes_varaveena = ["E3", "E3", "G3","G3","G3", "G3", "A3", "G3", "C4", "C4", "C4", "C4", "D4", "C4", "A3", "A3", "G3", "G3", "A3", "G3", "E3", "E3", "D3", "D3",
                "E3", "G3", "A3", "C4", "A3", "A3", "A3", "G3", "E3", "E3", "D3", "D3",
                "E3", "E3", "A3", "G3", "E3", "E3", "G3", "E3", "E3", "D3", "C3",
                "E3", "E3", "E3", "E3", "D3", "E3", "G3", "E3", "G3", "G3", "G3", "G3",
                "E3", "E3", "A3", "G3", "A3", "A3", "A3", "G3", "C4", "C4", "C4", "C4",
                "A3", "E4", "D4", "D4", "C4", "C4", "A3", "C4", "A3", "A3", "A3", "G3",
                "E3", "G3", "A3", "C4", "A3", "G3", "A3", "G3", "E3", "E3", "D3", "C3",
                "C3", "D3", "E3", "E3", "E3", "E3", "E3", "D3", "G3", "E3", "D3", "D3", "C3", "D3", "C3", "E3", "D3", "C3", "D3", "D3", "C3", "A2", "C3", "C3",]

Song2Notes_kundagaura = ["Ab3", "G3", "F3", "E3", "Db3", "C3", "Db3", "F3", "G3", "Ab3", "F3", "G3", "Ab3", "Db4", "Db4", "C4", "Ab3", "G3", "Ab3", "G3", "F3", "E3", "Db3", "C3", "C3", "C3", "Db3", "Db3", "Db3", "Db3", "Ab3", "G3", "F3", "E3", "Db3", "C3", "C3", "Db3", "G3", "F3", "E3", "Db3", "C3", "Db3", "E3", "Db3", "C3", "C3",]*3

bothSongs = Song1Notes_varaveena + Song2Notes_kundagaura

ourNotePlayingFunction(bothSongs*50)
