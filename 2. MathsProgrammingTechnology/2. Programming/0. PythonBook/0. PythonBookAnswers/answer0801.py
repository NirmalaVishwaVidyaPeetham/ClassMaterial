from pcinput import getInteger

# multiplicationtable gets an integer as parameter.
# It prints the multiplication table for that integer.
def multiplicationtable( n ):
    i = 1
    while i <= 10:
        print( i, "*", n, "=", i*n )
        i += 1

num = getInteger( "Give a number: " )
multiplicationtable( num )