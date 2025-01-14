import re

slist = re.findall( r"b[aeiou]ll", "Bill Gates and Uwe Boll \
drank Red Bull at a football match in Campbell." )
print( slist )