class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

pointlist = []

for i in range( 100 ):
    for j in range( 100 ):
        p = Point( i, j )
        pointlist.append( p )
        
print( "There are", len( pointlist ), "points in the list" )