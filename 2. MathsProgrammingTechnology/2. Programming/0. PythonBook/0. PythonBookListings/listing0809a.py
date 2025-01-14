from math import sqrt

def pythagoras( a: int, b: int ) -> float:
    if a <= 0 or b <= 0:
        return -1
    return sqrt( a*a + b*b )

print( pythagoras( 3, 4 ) )