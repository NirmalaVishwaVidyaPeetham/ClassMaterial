from math import sqrt
from pcinput import getInteger

def pythagoras( a, b ):
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

num1 = getInteger( "Give side 1: " )
num2 = getInteger( "Give side 2: " )
num3 = pythagoras( num1, num2 )
if num3 < 0:
    print( "The numbers you provided cannot be used." )
else:
    print( "The diagonal side's length is", num3 )