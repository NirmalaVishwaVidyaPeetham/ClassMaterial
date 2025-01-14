# The function gregoryLeibnitz approximates pi using the Gregory-
# Leibnitz series. It gets one parameter, which is an integer 
# that indicates how many terms are calculated. It returns the 
# approximation as a float.
def gregoryLeibnitz( num ):
    appr = 0
    for i in range( num ):
        if i%2 == 0:
            appr += 1/(1 + i*2)
        else:
            appr -= 1/(1 + i*2)
    return 4*appr

print( gregoryLeibnitz( 50 ) )