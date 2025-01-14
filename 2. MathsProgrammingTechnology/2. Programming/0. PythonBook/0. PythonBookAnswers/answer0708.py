from random import randint
from pcinput import getInteger

answer = randint( 1, 1000 )
count = 0

while True:
    guess = getInteger( "What is your guess? " )
    if guess < 1 or guess > 1000:
        print( "Your guess should be between 1 and 1000" )
        continue
    count += 1
    if guess < answer:
        print( "Higher" )
    elif guess > answer:
        print( "Lower" )
    else:
        print( "You guessed it!" )
        break
        
if count == 1:
    print( "You needed only one guess. Lucky bastard." )
else:
    print( "You needed", count, "guesses." )