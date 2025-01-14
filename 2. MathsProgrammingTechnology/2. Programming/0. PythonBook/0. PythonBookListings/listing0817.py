def isEven( num ):
    return num%2 == 0

if __name__ == '__main__':
    for i in range( 10 ):
        if isEven( i ):
            print( i, "is even" )