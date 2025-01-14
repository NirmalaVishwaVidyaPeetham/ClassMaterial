from itertools import combinations

numlist = [ 3, 8, -1, 4, -5, 6 ]
solution = []

for i in range( 1, len( numlist )+1 ):
    seq = combinations( numlist, i )
    for item in seq:
        if sum( item ) == 0:
            solution = item
            break
    if len( solution ) > 0:
        break
        
if len( solution ) <= 0:
    print( "There is no subset which adds up to zero" )
else:
    for i in range( len( solution ) ):
        if solution[i] < 0 or i == 0:
            print( solution[i], end="" )
        else:
            print( "+{}".format( solution[i] ), end="" )
    print( "=0" )