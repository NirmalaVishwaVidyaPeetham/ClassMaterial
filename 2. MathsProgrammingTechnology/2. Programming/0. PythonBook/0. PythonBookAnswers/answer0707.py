from random import random

DARTS = 100000
hits = 0
for i in range( DARTS ):
    x = random()
    y = random()
    if x*x + y*y < 1:
        hits += 1
        
print( "A reasonable approximation of pi is", 4 * hits / DARTS )