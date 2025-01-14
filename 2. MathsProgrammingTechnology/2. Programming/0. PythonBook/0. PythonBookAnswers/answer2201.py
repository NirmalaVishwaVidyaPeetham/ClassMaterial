class Rectangle:
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