from random import randint

TRIALS = 10000
DICE = 5
success = 0

for i in range( TRIALS ):
    lastdie = 0
    for j in range( DICE ):
        roll = randint( 1, 6 )
        if roll < lastdie:
            break
        lastdie = roll
    else:
        success += 1
        
print( "The probability of an increasing sequence",
    "of five die rolls is {:.3f}".format( success/TRIALS ) )