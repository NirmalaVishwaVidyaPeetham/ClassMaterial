try:
    fp = open( "NotAFile" )
    fp.close()
except IOError as ex:
    print( ex.args )