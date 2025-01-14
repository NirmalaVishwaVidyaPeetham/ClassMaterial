import re

pAplus = re.compile( r"a+" )
lAplus = pAplus.findall( "aardvark" )
print( lAplus )