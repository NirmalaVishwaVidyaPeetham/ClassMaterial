FILENAME = "pc_rose_copy.txt"

def display_contents( filename ):
    fp = open( filename, "rb" )
    print( fp.read() )
    fp.close()
    
def encrypt( filename ):
    fp = open( filename, "r+b" )
    buffer = fp.read()
    fp.seek(0)
    for c in buffer:
        if c >= 128:
            fp.write( bytes( [c-128] ) )
        else:
            fp.write( bytes( [c+128] ) )
    fp.close()
    
display_contents( FILENAME )
encrypt( FILENAME )
display_contents( FILENAME )