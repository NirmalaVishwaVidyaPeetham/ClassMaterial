import re

m = re.search( r"(\S).*\1", "Monty Python's Flying Circus" )
if m:
    print( "The character {} occurs twice".format( m.group(1) ) )
else:
    print( "No match was found." )