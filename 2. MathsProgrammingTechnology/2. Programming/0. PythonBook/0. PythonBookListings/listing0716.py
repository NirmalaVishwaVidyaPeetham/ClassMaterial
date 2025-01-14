from random import randint

TESTS = 10000

success = 0
for i in range( TESTS ):
    for j in range( 5 ):
        if randint( 1, 6 ) != 6:
            break
    else:
        success += 1

print( "Chance at five sixes is", success / TESTS )