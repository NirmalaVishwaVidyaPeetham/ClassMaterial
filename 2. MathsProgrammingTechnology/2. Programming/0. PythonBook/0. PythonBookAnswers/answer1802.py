letters = "etaoinshrdlcum "
unencoded = "Hello, world!"

# Print the unencoded string, as a check.
print( unencoded, len( unencoded ) )

# Create a half-byte-list as a basis for the encoding.
halfbytelist = []
for c in unencoded:
    if c in letters:
        halfbytelist.append( letters.index( c )+1 )
    else:
        byte = ord( c )
        halfbytelist.extend( [0, int( byte/16 ), byte%16 ] )
if len( halfbytelist )%2 != 0:
    halfbytelist.append( 0 )

# Turn the half-byte-list into a byte-list.
bytelist = []
for i in range( 0, len( halfbytelist ), 2 ):
    bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )

# Turn the byte-list into a byte string and print it, as a check. 
encoded = bytes( bytelist )
print( encoded, len( encoded ) )