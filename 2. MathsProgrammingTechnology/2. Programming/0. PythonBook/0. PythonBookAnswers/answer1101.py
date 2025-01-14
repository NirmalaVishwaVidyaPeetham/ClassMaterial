def add_complex( c1, c2 ):
    return (c1[0] + c2[0], c1[1] + c2[1])

def display_complex( c ):
    s = "("
    if c[1] == 0:
        return str( c[0] )
    elif c[0] != 0:
        s += str( c[0] )
        if c[1] > 0:
            s += "+"
    if c[1] != 1:
        if c[1] == -1:
            s += "-"
        else:
            s += str( c[1] )
    s += "i)"
    return s

num1 = (2,1)
num2 = (0,2)
print( display_complex( num1 ), "+", display_complex( num2 ), 
    "=", display_complex( add_complex( num1, num2 ) ) )