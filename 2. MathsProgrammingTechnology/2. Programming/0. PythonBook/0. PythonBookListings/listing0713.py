from pcinput import getInteger

x = getInteger( "Enter number 1: " )
y = getInteger( "Enter number 2: " )

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Numbers should both be between 0 and 1000" )
        x = getInteger( "Enter number 1: " )
        y = getInteger( "Enter number 2: " )
        continue
    print( "Multiplication of", x, "and", y, "gives", x * y )
    x = getInteger( "Enter number 1: " )
    y = getInteger( "Enter number 2: " )

if x == 0 or y == 0:
    print( "Goodbye!" )
else:
    print( "Error: the numbers cannot be dividers" )