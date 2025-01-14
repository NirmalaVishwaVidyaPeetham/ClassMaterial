# Calculates the factorial of parameter n, which must be an 
# integer. Returns the value of the factorial as an integer.
def factorial( n ):
    value = 1
    for i in range( 2, n+1 ):
        value *= i
    return value

# Calculates n over k; parameters n and k are integers. Returns 
# the value n over k as an integer (because it always must be 
# an integer).
def binomialCoefficient( n, k ):
    if k > n:
        return 0
    return int( factorial( n ) / 
        (factorial( k )*factorial( n - k )) )

def main():
    print( factorial( 5 ) )
    print( binomialCoefficient( 8, 3 ) )
    
if __name__ == '__main__':
    main()