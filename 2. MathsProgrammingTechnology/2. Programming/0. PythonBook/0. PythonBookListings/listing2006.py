from math import sqrt

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def distance_from_origin( self ):
        return sqrt( self.x*self.x + self.y*self.y )

p = Point( 3.5, 5.0 )
print( p.distance_from_origin() )