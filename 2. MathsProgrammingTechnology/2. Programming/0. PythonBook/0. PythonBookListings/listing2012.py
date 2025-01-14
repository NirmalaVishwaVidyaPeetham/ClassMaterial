class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

totalx = 0
totaly = 0 

for i in range( 1000 ):
    for j in range( 1000 ):
        p = Point( i, j )
        totalx += p.x
        totaly += p.y
        
print( "The totals of x and y are", totalx, "and", totaly )