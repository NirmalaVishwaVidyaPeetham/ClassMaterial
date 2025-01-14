import re

sentence = "Michael Jordan, Bill Gates, and the Dalai Lama \
decided to take a plane trip together."

pname = re.compile( r"\b([A-Z][a-z]*\s+[A-Z][a-z]*)\b" )
namelist = pname.findall( sentence )
for name in namelist:
    print( name )