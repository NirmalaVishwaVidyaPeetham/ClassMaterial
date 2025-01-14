from itertools import permutations

SIZE = 8 # Board size.

def display_board( columns ):
    for i in columns :
        for j in range( len( columns ) ):
            if i == j:
                print( 'Q', end=" " )
            else:
                print( '-', end=" " )
        print()

def is_solution( columns ):
    for row in range( len( columns ) ):
        col = columns[row]
        for i in range( row+1, len( columns ) ):
            if i - row == abs( columns[i] - col ):
                return False
    return True
        
columns = list( range( SIZE ) )

for p in permutations( columns ):
    if is_solution( p ):
        display_board( p )
        break
else:
    print( "No solutions found" ) # Should not happen.