class MesosticWord:
    def __init__( self,  word, index, question ):
        self.word = word
        self.index = index
        self.question = question

class Mesostic:
    def __init__( self, name, words ):
        self.name, self.words = name, words
    def __len__( self ):
        return len( self.words )
    def __getitem__( self, n ):
        return self.words[n]
    def __setitem__( self, n, value ):
        self.words[n] = value
    def __delitem__( self, n ):
        del self.words[n]
    def display( self ):
        print( self.name )
        for i in range( len( self ) ):
            print( "{}. {}".format( i+1, self[i].question ), 
                end = "  " )
            for j in range( len( self[i].word ) ):
                if j == self[i].index:
                    print( "* ", end="" )
                else:
                    print( "_ ", end="" )
            print()
    def solution( self ):
        s = ""
        for i in range( len( self ) ):
            s += self[i].word[self[i].index]
        return s
    
puzzle = Mesostic( 
    "The Monty Python and the Holy Grail Mesostic Puzzle",
    [ MesosticWord( "ANTHRAX", 5, 
          "Sir Galahad's tale took place in the Castle" ),
      MesosticWord( "PERIL", 2, 
          "Sir Robin was thrown into the Gorge of Eternal" ),
      MesosticWord( "RABBIT", 5, 
          "Sir Bors was killed by a" ),
      MesosticWord( "SHRUBBERY", 1, 
          "The Knights of Ni!'s first demand was to get a" ),
      MesosticWord( "COCONUT", 5, 
          "A horse can be replaced by a" ),
      MesosticWord( "MINSTRELS", 5, 
          "They were forced to eat Robin's" ) ] )

puzzle.display()