import re

sentence = "The price of a 2-room apartment in Manhattan \
starts at 1 million dollars, and may actually be the 10-fold \
of that on 42nd Street."

pword = re.compile( r"[A-Za-z]+" )
wordlist = pword.findall( sentence )
for word in wordlist:
    print( word )