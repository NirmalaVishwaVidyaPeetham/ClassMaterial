from pcinput import getFloat
from math import sqrt

side1 = getFloat( "Please enter the length of the first side: " )
side2 = getFloat( "Please enter the length of the second side: ")
side3 = sqrt( side1 * side1 + side2 * side2 )
print( "The length of the diagonal is {:.3f}.".format( side3 ) )
