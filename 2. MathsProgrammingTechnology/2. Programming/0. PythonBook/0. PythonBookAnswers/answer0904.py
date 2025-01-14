def gcd( m, n ):
    if m % n == 0:
        return n
    return gcd( n, m%n )
    
print( gcd( 7*5*13, 2*3*7*11 ) )