from collections import Counter

sentence = "Your mother was a hamster and \
your father smelled of elderberries."
sentence2 = ""
for c in sentence.lower():
    if c >= 'a' and c <= 'z':
        sentence2 += c

clist = Counter( sentence2 ).most_common( 5 )
for c in clist:
    print( "{}: {}".format( c[0], c[1] ) )