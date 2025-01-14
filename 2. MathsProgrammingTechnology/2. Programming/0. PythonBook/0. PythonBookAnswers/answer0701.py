from pcinput import getInteger

num = getInteger( "Give a number: " )
i = 1
while i <= 10:
    print( i, "*", num, "=", i*num )
    i += 1