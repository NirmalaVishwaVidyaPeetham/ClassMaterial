SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit
        self.rank = rank
    def __repr__( self ):
        return "({},{})".format( self.suit, self.rank )
    def __str__( self ):
        return "{} of {}".format(
            RANKS[self.rank], SUITS[self.suit] )
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
    
dp1 = Drawpile( [Card(3,0), Card(0,11), Card(2,5)] )
dp2 = Drawpile( [Card(3,2), Card(3,1), Card(1,6)] )

i = 1
while len( dp1 ) > 0 and len( dp2 ) > 0:
    print( "Round", i )
    print( "Deck1:", dp1 )
    print( "Deck2:", dp2 )
    c1 = dp1.draw()
    c2 = dp2.draw()
    if c1 > c2:
        dp1.add( c1 )
        dp1.add( c2 )
    else:
        dp2.add( c2 )
        dp2.add( c1 )
    i += 1
        
print( "The game has ended" )
if len( dp1 ) > 0:
    print( "Deck1:", dp1 )
    print( "The first deck wins!" )
else:
    print( "Deck2:", dp2 )
    print( "The second deck wins!" )