# Recursive function that determines if intlist, which is a list 
# of integers, contains a subset that adds up to total. It  
# returns the subset, or empty list if there is no such subset.
def subset_that_adds_up_to( intlist, total ):
    for num in intlist:
        if num == total:
            return [num]
        newlist = intlist[:]
        newlist.remove( num )
        retlist = subset_that_adds_up_to( newlist, total-num )
        if len( retlist ) > 0:
            retlist.insert( 0, num )
            return( retlist )
    return []

numlist = [ 3, 8, -1, 4, -5, 6 ]

solution = subset_that_adds_up_to( numlist, 0 )

if len( solution ) <= 0:
    print( "There is no subset which adds up to zero" )
else:
    for i in range( len( solution ) ):
        if solution[i] < 0 or i == 0:
            print( solution[i], end="" )
        else:
            print( "+{}".format( solution[i] ), end="" )
    print( "=0" )