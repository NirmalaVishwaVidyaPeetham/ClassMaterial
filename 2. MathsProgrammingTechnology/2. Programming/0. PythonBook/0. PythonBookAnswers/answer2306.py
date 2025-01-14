from itertools import combinations

testdict = {"a":1, "b":2, "c":3, "d":4 }
result = [ {} ]

keylist = list( testdict.keys() )
for length in range( 1, len( testdict)+1 ):
    for item in combinations( keylist, length ):
        subdict = {}
        for key in item:
            subdict[key] = testdict[key]
        result.append( subdict )

print( result )