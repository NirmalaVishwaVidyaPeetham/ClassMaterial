from math import pi

class Shape:
    def area( self ):
        return NotImplemented
    def circumference( self ):
        return NotImplemented

class Circle( Shape ):
    def __init__( self, x, y, r ):
        self.x, self.y, self.r = x, y, r
    def __repr__( self ):
        return "[({},{}),r={}]".format( self.x, self.y, self.r )
    def area( self ):
        return pi * self.r * self.r
    def circumference( self ):
        return 2 * pi * self.r
    
class Rectangle( Shape ):
    def __init__( self, x, y, w, h ):
        self.x, self.y, self.w, self.h = x, y, w, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
            self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)

class Square( Rectangle ):
    def __init__( self, x, y, w ):
        super().__init__( x, y, w, w )
        
s = Square( 1, 1, 4 )
print( s, s.area(), s.circumference() )
c = Circle( 1, 1, 4 )
print( c, c.area(), c.circumference() )