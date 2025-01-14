from pcinput import getString, getLetter
from os.path import exists, getsize

LETTERS = b"etaoinshrdlcum "

# Compress byte string unencoded, return the compressed version.
def compress( unencoded ):
    halfbytelist = []
    for c in unencoded:
        if c in LETTERS:
            halfbytelist.append( LETTERS.index( c )+1 )
        else:
            halfbytelist.extend( [0, int( c/16 ), c%16 ] )
    if len( halfbytelist )%2 != 0:
        halfbytelist.append( 0 )
    bytelist = []
    for i in range( 0, len( halfbytelist ), 2 ):
        bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )
    return bytes( bytelist )

# Decompress byte string encoded, return decompressed version.
def decompress( encoded ):
    halfbytelist = []
    for c in encoded:
        halfbytelist.extend( [ int( c/16 ), c%16 ] )
    if halfbytelist[-1] == 0:
        del halfbytelist[-1]
    bytelist = []
    while len( halfbytelist ) > 0:
        num = halfbytelist.pop(0)
        if num > 0:
            bytelist.append( LETTERS[num-1] )
            continue
        num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
        bytelist.append( num )
    return bytes( bytelist )

# Ask for the input file and read its contents.
while True:
    filein = getString( "Which is the input file? " )
    if not exists( filein ):
        print( filein, "does not exist" )
        continue
    try:
        fp = open( filein, "rb" )
        buffer = fp.read()
        fp.close()
    except IOError as ex:
        print( filein, "cannot be processed, choose another" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break
    
# Ask for the output file and create it.
while True:
    fileout = getString( "Which is the output file? " )
    if exists( fileout ):
        print( fileout, "already exists" )
        continue
    try:
        fp = open( fileout, "wb" )
    except IOError as ex:
        print( fileout, "cannot be created,",
            "choose another file name" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Ask whether the user wants to compress or decompress.
while True:
    dc = getLetter( "Choose (C)ompress or (D)ecompress? " )
    if dc != 'C' and dc != 'D':
        print( "Please choose C or D" )
        continue
    break
    
# Compress or decompress the buffer.
if dc == 'C':
    buffer = compress( buffer )
else:
    buffer = decompress( buffer )
    
# Store the (de)compressed buffer in the output file.
try:
    fp.write( buffer )
    fp.close()
except IOError as ex:
    print( "The writing process failed" )
    print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))

# Report the sizes of input and output.
print( getsize( filein ), "bytes read" )
print( getsize( fileout ), "bytes written" )