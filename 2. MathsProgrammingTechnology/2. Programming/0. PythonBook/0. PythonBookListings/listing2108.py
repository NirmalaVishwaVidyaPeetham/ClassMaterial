class Sentence:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )

s = Sentence( [ "There", "is", "only", "one", "thing", "worse", 
"than", "being", "talked", "about", 
"and", "that", "is", "not", "being", "talked", "about" ] )
print( s )
print( len( s ) )
print( s[5] )
s[5] = "better"
print( "being" in s )