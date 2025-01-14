from collections import Counter
from pcinput import getInteger
from statistics import mean, median
from sys import exit

numlist = []
while True:
    num = getInteger( "Enter a number: " )
    if num == 0:
        break
    numlist.append( num )

if len( numlist ) <= 0:
    print( "No numbers were entered" )
    exit()
    
print( "Mean:", mean( numlist ) )
print( "Median:", median( numlist ) )

clist = Counter( numlist ).most_common()
if clist[0][1] <= 1:
    print( "There is no mode" )
else:
    mlist = [str( x[0] ) for x in clist if x[1] == clist[0][1] ]
    s = ", ".join( mlist )
    print( "Mode:", s )