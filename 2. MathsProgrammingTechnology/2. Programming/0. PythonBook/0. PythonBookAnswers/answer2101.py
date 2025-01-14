SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit # used as index in the SUITS list
        self.rank = rank # used as index in the RANKS list
    def __repr__( self ):
        return "({},{})".format( self.suit, self.rank )
    def __str__( self ):
        return "{} of {}".format( RANKS[self.rank], \
            SUITS[self.suit] )
    def __eq__( self, c ):
        if isinstance( c, Card ):
            return self.rank == c.rank
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Card ):
            return self.rank > c.rank
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Card ):
            return self.rank >= c.rank
        return NotImplemented
    
c5 = Card( 2, 3 )
d5 = Card( 3, 3 )
sk = Card( 1, 11 )
print( "{}, {}, {}".format( c5, d5, sk ) )
print( c5 == d5 )
print( c5 == sk )
print( c5 > sk )
print( c5 >= sk )
print( c5 < sk )
print( c5 <= sk )