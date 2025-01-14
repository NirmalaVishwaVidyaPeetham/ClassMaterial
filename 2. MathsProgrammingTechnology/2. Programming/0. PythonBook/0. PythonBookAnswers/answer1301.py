text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def clean( s ):
    news = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z":
            news += c
        else:
            news += " "
    return news

worddict = {}
for word in clean( text ).split():
    worddict[word] = worddict.get( word, 0 ) + 1
    
keylist = list( worddict.keys() )
keylist.sort()
for key in keylist:
    print( "{}: {}".format( key, worddict[key] ) )