FILENAME = "pc_writetest.tmp"

def displaycontents( filename ):
    fp = open( filename )
    print( fp.read() )
    fp.close()

displaycontents( FILENAME )

fp = open( FILENAME, "a" )
while True:
    text = input( "Please enter a line of text: " )
    if text == "":
        break
    fp.write( text+"\n" )
fp.close()

displaycontents( FILENAME )