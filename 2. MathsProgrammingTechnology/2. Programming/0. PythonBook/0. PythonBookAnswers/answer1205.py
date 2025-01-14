numbers = 101 * [True]
numbers[1] = False
for i in range( 1, len( numbers ) ):
    if not numbers[i]:
        continue
    print( i, end=" " )
    j = 2
    while j*i < len( numbers ):
        numbers[j*i] = False
        j += 1