fp = open( "pc_binarytest.tmp", "rb" )
print( "1. Current position of the file pointer is", fp.tell() )
fp.seek( 50 )
print( "2. Current position of the file pointer is", fp.tell() )
buffer = fp.read( 23 )
print( "3. Current position of the file pointer is", fp.tell() )
fp.close()

print( buffer )
s = ""
for c in buffer:
    s += chr( c-128 )
print( "The secret words are:", s )