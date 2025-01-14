from random import random

COOPERATE = 'C'
DEFECT = 'D'
ROUNDS = 100

class Strategy:
    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def choice( self ):
        # Should return COOPERATE or DEFECT
        return NotImplemented
    def lastmove( self, mymove, opponentmove ):
        # Gets passed the last move made, after call to choice()
        pass
    def incscore( self, n ):
        self.score += n
        
class AlwaysDefect( Strategy ):
    def choice( self ):
        return DEFECT
        
class Random( Strategy ):
    def choice( self ):
        if random() >= 0.5:
            return COOPERATE
        return DEFECT

class MemoryStrategy( Strategy ):
    def __init__( self, name="" ):
        super().__init__( name )
        self.history = []
    def lastmove( self, mymove, opponentmove ):
        self.history.append( (mymove, opponentmove) )
        
class TitForTat( MemoryStrategy ):
    def choice( self ):
        if len( self.history ) < 1:
            return COOPERATE
        return self.history[-1][1]

class TitForTwoTats( MemoryStrategy ):
    def choice( self ):
        if len( self.history ) < 2:
            return COOPERATE
        if self.history[-1][1] == DEFECT and \
            self.history[-2][1] == DEFECT:
            return DEFECT
        return COOPERATE

class Majority( MemoryStrategy ):
    def choice( self ):
        countD = 0
        for i in range( len( self.history ) ):
            if self.history[i][1] == DEFECT:
                countD += 1
        if countD > len( self.history ) / 2:
            return DEFECT
        return COOPERATE
            
strategy1 = AlwaysDefect( "Always Defect" )
strategy2 = Majority( "Majority" )

for i in range( ROUNDS ):
    c1 = strategy1.choice()
    c2 = strategy2.choice()
    if c1 == c2:
        strategy1.incscore( 3 if c1 == COOPERATE else 1 )
        strategy2.incscore( 3 if c2 == COOPERATE else 1 )
    else:
        strategy1.incscore( 0 if c1 == COOPERATE else 6 )
        strategy2.incscore( 0 if c2 == COOPERATE else 6 )
    strategy1.lastmove( c1, c2 )
    strategy2.lastmove( c2, c1 )
        
print( "Score of", strategy1.name, "is", strategy1.score )
print( "Score of", strategy2.name, "is", strategy2.score )