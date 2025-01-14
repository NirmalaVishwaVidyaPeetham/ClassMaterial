import errno

try:
    fp = open( "NotAFile" )
    fp.close()
except IOError as ex:
    if ex.args[0] == errno.ENOENT:
        print( "File not found!" )
    else:
        print( ex.args[0], ex.args[1] )