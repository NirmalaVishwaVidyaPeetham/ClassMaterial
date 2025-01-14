from os.path import join
from os import getcwd

files = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
letterlist = [ len( files )*[0] for i in range( 26 ) ]
totallist = len( files ) * [0]

# Process all the input files, read their contents line by line,
# make them lower case, and keep track of the letter counts in 
# letterlist, while keeping track of total counts in totallist.
filecount = 0
for name in files:
    filename = join( getcwd(), name )
    fp = open( filename )
    while True:
        line = fp.readline()
        if line == "":
            break
        line = line.lower()
        for c in line:
            if c >= 'a' and c <= 'z':
                totallist[filecount] += 1
                letterlist[ord(c)-ord("a")][filecount] += 1
    fp.close()
    filecount += 1

# Write the counts in CSV format.
outfilename = join( getcwd(), "pc_writetest.csv" )
fp = open( outfilename, "w" )
for i in range( len( letterlist ) ):
    s = "\"{}\"".format( chr( ord("a")+i ) )
    for j in range( len( files ) ):
        s += ",{:.5f}".format( letterlist[i][j]/totallist[j] )
    fp.write( s+"\n" )
fp.close()

# Print the contents of the created output file as a check.
fp = open( outfilename )
print( fp.read() )
fp.close()