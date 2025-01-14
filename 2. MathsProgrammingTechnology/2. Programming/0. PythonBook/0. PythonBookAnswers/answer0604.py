from pcinput import getFloat
from math import sqrt

a = getFloat( "A: " )
b = getFloat( "B: " )
c = getFloat( "C: " )

if a == 0:
    if b == 0:
        print( "There is not even an unknown in this equation!" )
    else:
        print( "There is one solution, namely", -c/b )
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print( "There are no solutions" )
    elif discriminant == 0:
        print( "There is one solution, namely", -b/(2*a) )
    else:
        print( "There are two solutions, namely",  
                (-b+sqrt(discriminant))/(2*a), "and", 
                (-b-sqrt(discriminant))/(2*a) )