from pcinput import getInteger

num = getInteger( "Give a number: " )
for i in range( 1, 11 ):
    print( i, "*", num, "=", i*num )