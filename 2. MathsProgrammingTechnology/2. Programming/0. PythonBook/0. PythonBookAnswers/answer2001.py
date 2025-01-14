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
        self.width = abs( width )
        self.height = abs( height )
        if self.width == 0:
            self.width = 1
        if self.height == 0:
            self.height = 1
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, 
            self.width, self.height )
    def surface_area( self ):
        return self.width * self.height
    def circumference( self ):
        return 2*(self.width + self.height)
    def bottom_right( self ):
        return Point( self.point.x + self.width, 
            self.point.y + self.height )
    def overlap( self,r ):
        r1, r2 = self, r
        if self.point.x > r.point.x or \
            (self.point.x == r.point.x and \
            self.point.y > r.point.y):
            r1, r2 = r, self
        if r1.bottom_right().x <= r2.point.x or \
            r1.bottom_right().y <= r2.point.y:
            return None
        return Rectangle( r2.point, 
            min( r1.bottom_right().x - r2.point.x, r2.width ), 
            min( r1.bottom_right().y - r2.point.y, r2.height ) )
    
r1 = Rectangle( Point( 1, 1 ), 8, 5 )
r2 = Rectangle( Point( 2, 3 ), 9, 2 )

print( r1.surface_area() )
print( r1.circumference() )
print( r1.bottom_right() )
r = r1.overlap( r2 )
if r:
    print( r )
else:
    print( "There is no overlap for the rectangles" )