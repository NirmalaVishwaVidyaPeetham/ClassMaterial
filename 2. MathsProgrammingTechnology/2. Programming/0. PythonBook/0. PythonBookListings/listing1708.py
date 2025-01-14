try:
    print( int( "NotAnInteger" ) )
except ValueError as ex:
    print( ex.args )