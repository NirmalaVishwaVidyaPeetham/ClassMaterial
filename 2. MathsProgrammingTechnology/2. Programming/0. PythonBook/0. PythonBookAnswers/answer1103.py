inttuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 
    13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )

def display_inttuple( it ):
    for element in it:
        if isinstance( element, int ):
            print( element, end=" ")
        else:
            display_inttuple( element )

display_inttuple( inttuple )