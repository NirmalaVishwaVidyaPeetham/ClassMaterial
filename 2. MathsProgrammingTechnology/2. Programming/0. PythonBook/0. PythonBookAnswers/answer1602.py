def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

wdict = {}
fp = open( "pc_woodchuck.txt" )
while True:
    line = fp.readline()
    if line == "":
        break
    for word in clean( line ).split():
        wdict[word] = wdict.get( word, 0 ) + 1
fp.close()
    
keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )