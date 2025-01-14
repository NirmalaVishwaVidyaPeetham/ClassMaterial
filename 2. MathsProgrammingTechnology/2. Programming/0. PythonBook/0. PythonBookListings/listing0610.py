x = 5
y = 0
match (x,y):
    case (0,0):
        print( "x and y are both 0" )
    case (0,_):
        print( "x is 0" )
    case (_,0):
        print( "y is 0" )
    case other:
        print( "neither x nor y is 0" )