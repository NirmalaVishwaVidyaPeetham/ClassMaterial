from collections import Counter

data = [ "apple", "banana", "apple", "banana", "apple", "cherry" ]
c = Counter( data )
print( c )
print( c.most_common( 1 ) )

data2 = [ "orange", "cherry", "cherry", "cherry", "cherry" ]
c.update( data2 )
print( c )
print( c.most_common() )