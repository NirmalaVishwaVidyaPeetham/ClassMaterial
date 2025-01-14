def setBit( store, index, value ):
    mask = 1<<index
    if value:
        store |= mask
    else:
        store &= ~mask
    return store

# getBit() returns 0 when the bit corresponding to index is set,
# and something else otherwise. As only 0 is interpreted as False
# this function can be used to test the value of the bit.
def getBit( store, index ):
    mask = 1<<index
    return store & mask

def displayBits( store ):
    for i in range( 8 ):
        index = 7 - i
        if getBit( store, index ):
            print( "1", end="" )
        else:
            print( "0", end="" )
    print()
    
store = 0
store = setBit( store, 0, True )
store = setBit( store, 1, True )
store = setBit( store, 2, False )
store = setBit( store, 3, True )
store = setBit( store, 4, False )
store = setBit( store, 5, True )
displayBits( store )

store = setBit( store, 1, False )
displayBits( store )