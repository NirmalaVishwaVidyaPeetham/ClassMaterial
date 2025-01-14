from pickle import dump

cheeseshop = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

fp = open( "pc_cheese.pck", "wb" )
dump( cheeseshop, fp )
fp.close()

print( "Cheeseshop was pickled" )