from json import dump, load

cheeseshop = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.json", "w" )
dump( cheeseshop, fp )
fp.close()

fp = open( "pc_cheese.json", "r" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )