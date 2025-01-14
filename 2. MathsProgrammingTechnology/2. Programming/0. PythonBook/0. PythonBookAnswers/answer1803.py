letters = "etaoinshrdlcum "
encoded = b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'

# Print the encoded byte string, as a check.
print( encoded, len( encoded ) )

# Create a half-byte-list on the basis of the byte string.
halfbytelist = []
for c in encoded:
    halfbytelist.extend( [ int( c/16 ), c%16 ] )
if halfbytelist[-1] == 0:
    del halfbytelist[-1]
    
# Turn the half-byte-list into a string.
decoded = ""
while len( halfbytelist ) > 0:
    num = halfbytelist.pop(0)
    if num > 0:
        decoded += letters[num-1]
        continue
    num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
    decoded += chr( num )

# Print the string, as a check.
print( decoded, len( decoded ) )