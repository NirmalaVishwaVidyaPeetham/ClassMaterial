from os.path import join
from os import getcwd

def removevowels( line ):
    newline = ""
    for c in line:
        if c not in "aeiouAEIOU":
            newline += c
    return newline

inputname = join( getcwd(), "pc_woodchuck.txt" )
outputname = join( getcwd(), "pc_woodchuck.tmp" )

fpi = open( inputname )
fpo = open( outputname, "w" )

countread = 0
countwritten = 0

while True:
    line = fpi.readline()
    if line == "":
        break
    countread += len( line )
    line = removevowels( line )
    fpo.write( line )
    countwritten += len( line )

fpo.close()
fpi.close()

print( "Characters read:", countread )
print( "Characters written:", countwritten )