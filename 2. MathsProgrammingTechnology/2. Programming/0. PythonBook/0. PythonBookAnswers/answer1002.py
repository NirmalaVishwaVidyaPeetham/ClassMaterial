text = """And sending tinted postcards of places they don't 
realise they haven't even visited to 'All at nu[m]ber 22, weather 
w[on]derful, our room is marked with an 'X'. Wish you were here. 
Food very greasy but we've found a charming li[t]tle local place 
hidden awa[y ]in the back streets where they serve Watney's Red 
Barrel and cheese and onion cris[p]s and the accordionist pla[y]s 
"Maybe i[t]'s because I'm a Londoner"' and spending four days on 
the tarmac at Luton airport on a five-day package tour wit[h] 
n[o]thing to eat but dried Watney's sa[n]dwiches..."""

start = -1
while True:
    start = text.find( "[", start+1 )
    if start < 0:
        break
    finish = text.find( "]", start )
    if finish < 0:
        break
    print( text[start+1:finish], end="" )
    start = finish 
print()