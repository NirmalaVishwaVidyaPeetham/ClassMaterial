from csv import reader
from json import dump

data = []

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for line in csvreader:
    data.append( line )
fp.close()

fp = open( "pc_writetest.json", "w" )
dump( data, fp )
fp.close()

fp = open( "pc_writetest.json" )
print( fp.read() )
fp.close()