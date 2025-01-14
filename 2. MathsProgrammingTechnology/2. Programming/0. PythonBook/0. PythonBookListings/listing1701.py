from pcinput import getInteger

num = getInteger( "Please enter a number: " )
try:
    print( "3 divided by {} is {}".format( num, 3/num ) )
except:
    print( "Division by zero is not allowed" )
print( "Goodbye!" )