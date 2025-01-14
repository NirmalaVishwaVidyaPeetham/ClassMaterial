from pcinput import getFloat
from math import sqrt

# This function solves a quadratic equation.
# Its parameters are the numeric values for A, B, and C in the 
# equation Ax**2 + Bx + C = 0. It returns three values: an int 
# 0, 1, or 2, indicating the number of solutions, followed by two 
# numbers which are the solutions. With no solutions, both 
# solutions are set to zero. With one solution, it is returned as 
# the first of the two, while the other is set to zero.
def quadraticFormula( a, b, c ):
    if a == 0:
        if b == 0:
            return 0, 0, 0
        return 1, -c/b, 0
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return 0, 0, 0
    elif discriminant == 0:
        return 1, -b/(2*a), 0
    else:
        return 2, (-b+sqrt(discriminant))/(2*a), \
            (-b-sqrt(discriminant))/(2*a)
    
num, sol1, sol2 = quadraticFormula( getFloat( "A: " ), 
    getFloat( "B: " ), getFloat( "C: " ) )
if num == 0:
    print( "There are no solutions" )
elif num == 1:
    print( "There is one solution, namely:", sol1 )
else:
    print( "There are two solutions, namely:", sol1, "and", sol2)