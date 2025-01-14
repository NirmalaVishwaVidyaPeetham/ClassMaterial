from copy import copy

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = copy( point )
        self.width = width
        self.height = height
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, 
            self.height )

p = Point( 3.5, 5.0 )
r = Rectangle( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )