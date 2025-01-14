from os.path import join
from os import getcwd

WORDLEN = 2

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

files = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
setlist = []

for name in files:
    filename = join( getcwd(), name )
    wordset = set()
    setlist.append( wordset )
    fp = open( filename )
    while True:
        line = fp.readline()
        if line == "":
            break
        wordlist = clean( line ).split()
        for word in wordlist:
            if len( word ) >= WORDLEN:
                wordset.add( word )
    fp.close()

combination = setlist[0].copy()
i = 1
while i < len( setlist ):
    combination = combination & setlist[i]
    i += 1
for word in combination:
    print( word )