fp = open( "pc_writetest.tmp", "w" )
while True:
    text = input( "Please enter a line of text: " )
    if text == "":
        break
    fp.write( text )
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )