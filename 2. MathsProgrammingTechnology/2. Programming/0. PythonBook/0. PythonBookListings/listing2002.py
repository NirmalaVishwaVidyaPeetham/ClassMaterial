class Point:
    def __init__( self, x, y ):
        self.x = x
        self.y = y

p = Point( 3.5, 5.0 )
print( "({}, {})".format( p.x, p.y ) )