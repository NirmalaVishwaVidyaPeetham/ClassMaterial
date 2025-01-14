SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit 
        self.rank = rank 
    def __str__( self ):
        return "{} of {}".format(
            RANKS[self.rank], SUITS[self.suit] )

class Drawpile:
    def __init__( self, pile=[] ):
        self.pile = pile
    def __len__( self ):
        return len( self.pile )
    def __getitem__( self, n ):
        return self.pile[n]
    def add( self, c ):
        self.pile.append( c )
    def draw( self ):
        if len( self ) <= 0:
            return None
        return self.pile.pop(0)
    def __repr__( self ):
        sep = ""
        s = ""
        for c in self.pile:
            s += sep + str( c )
            sep = ", "
        return s
    
dp1 = Drawpile( [Card(0,1), Card(0,5), Card(2,4), Card(1,12)] )
print( dp1 )
print( dp1[1] )
dp1.add( Card(3,12) )
print( dp1 )
print( dp1.draw() )
print( dp1 )