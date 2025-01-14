fp = open( "pc_rose.txt ")
try:
    buffer = fp.read()
    print( buffer )
except IOError:
    fp.close()
    raise
fp.close()