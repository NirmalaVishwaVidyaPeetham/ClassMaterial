def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

fp = open( "pc_woodchuck.txt" )
text = fp.read()
fp.close()

wdict = {}
for word in clean( text ).split():
    wdict[word] = wdict.get( word, 0 ) + 1
    
keylist = list( wdict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, wdict[key] ) )