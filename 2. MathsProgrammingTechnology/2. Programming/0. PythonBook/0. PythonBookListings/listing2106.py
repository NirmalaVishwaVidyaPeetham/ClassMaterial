class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({},{}i,{}j,{}k)".format( self.a, self.b, 
            self.c, self.d )
    def __neg__( self ):
        return Quaternion( -self.a, -self.b, -self.c, -self.d)
    def __abs__( self ):
        return Quaternion( abs( self.a ), abs( self.b ), 
            abs( self.c ), abs( self.d ) )
    def __bytes__( self ):
        return self.__str__().encode( "utf-8" )

c1 = Quaternion( 3, -4, 5, -6 )
print( c1 )
print( -c1 )
print( abs( c1 ) )
print( bytes( c1 ) )