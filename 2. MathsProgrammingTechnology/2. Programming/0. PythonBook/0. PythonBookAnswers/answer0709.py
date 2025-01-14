from pcinput import getLetter
from sys import exit

count = 0
lowest = 0
highest = 1001
print( "Take a number in mind between 1 and 1000." )

while True:
    guess = int( (lowest + highest) / 2 )
    prompt = "I guess "+str( guess )+". Is your number"+\
        " (L)ower or (H)igher, or is this (C)orrect? "
    response = getLetter( prompt )
    if response == "C":
        count += 1
        break
    elif response == "L":
        highest = guess
    elif response =="H":
        lowest = guess
    else:
        print( "Please enter H, L, or C." )
        continue
    count += 1
    if lowest >= highest-1:
        print( "You must have made a mistake,", 
            "because you said that the answer is higher than",
            lowest, "but also lower than", highest )
        print( "I quit this game" )
        exit()

if count == 1:
    print( "I needed only one guess! I must be a mind reader." )
else:
    print( "I needed", count, "guesses." )