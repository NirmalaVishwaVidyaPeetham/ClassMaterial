text = """Now, it's quite simple to defend yourself against a 
man armed with a banana. First of all you force him to drop 
the banana; then, second, you eat the banana, thus disarming 
him. You have now rendered him helpless."""

def count_letter( x ):
    return x[0], -ord(x[1]) 

countlist = []
for i in range( 26 ):
    countlist.append( [0, chr(ord("a")+i)] )
    
for letter in text.lower():
    if letter >= "a" and letter <= "z":
        countlist[ord(letter)-ord("a")][0] += 1
        
countlist.sort( reverse=True, key=count_letter )
    
for count in countlist:
    print( "{:3}: {}".format( count[0],count[1] ) )