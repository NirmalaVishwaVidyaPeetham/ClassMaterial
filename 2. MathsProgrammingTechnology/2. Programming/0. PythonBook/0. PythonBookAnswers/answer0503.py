from pcinput import getFloat

num1 = getFloat( "Please enter number 1: " )
num2 = getFloat( "Please enter number 2: " )
num3 = getFloat( "Please enter number 3: " )

print( "The largest is", max( num1, num2, num3 ) )
print( "The smallest is", min( num1, num2, num3 ) )
print( "The average is", round( (num1 + num2 + num3)/3, 2 ) )
