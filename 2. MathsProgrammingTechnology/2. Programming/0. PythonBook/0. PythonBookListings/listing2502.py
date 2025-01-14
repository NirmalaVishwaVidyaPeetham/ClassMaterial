import re

mlist = re.finditer( r"a+", 
    "Look out! A dangerous aardvark is on the loose!" )
for m in mlist:
    print( "{} starts at index {} and ends at index {}.".format( 
        m.group(), m.start(), m.end() ) )