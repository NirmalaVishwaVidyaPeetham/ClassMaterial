def multiply_complex( c1, c2 ):
    return (c1[0]*c2[0] - c2[1]*c1[1], c1[0]*c2[1] + c1[1]*c2[0])

def display_complex( c ):
    return "({},{}i)".format( c[0], c[1] )

num1 = (2,1)
num2 = (0,2)
print( display_complex( num1 ), "*", display_complex( num2 ), 
    "=", display_complex( multiply_complex( num1, num2 ) ) )