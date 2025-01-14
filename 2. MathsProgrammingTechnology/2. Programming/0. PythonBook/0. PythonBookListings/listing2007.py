from math import sqrt

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def translate( self, shift_x, shift_y ):
        self.x += shift_x
        self.y += shift_y

p = Point( 3.5, 5.0 )
p.translate( -3, 7 )
print( p )