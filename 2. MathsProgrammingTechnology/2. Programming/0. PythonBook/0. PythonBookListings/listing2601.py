from csv import reader

fp = open( "pc_inventory.csv", newline='' )
csvreader = reader( fp )
for line in csvreader:
    print( line )
fp.close()