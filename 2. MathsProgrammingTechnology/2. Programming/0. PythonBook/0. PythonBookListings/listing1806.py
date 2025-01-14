FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, encoding="latin-1" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer )
fp.close()