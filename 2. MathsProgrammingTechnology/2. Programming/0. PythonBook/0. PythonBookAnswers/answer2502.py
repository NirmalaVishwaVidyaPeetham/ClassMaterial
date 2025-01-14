import re

sentence = "The word ether can be found in my thesaurus \
using the archaic spelling 'aether'."

pthe = re.compile( r"\bthe\b", re.I )
thelist = pthe.findall( sentence )
print( len( thelist ) )