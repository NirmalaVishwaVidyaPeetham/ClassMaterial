from itertools import permutations

word = input( "Please enter a word: " )
seq = permutations( word )
for item in set( seq ):
    print( "".join( item ) )