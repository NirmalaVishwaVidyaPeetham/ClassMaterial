import re

pDate = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
m = pDate.search( "In response to your letter of 25-3-2015, \
I decided to hire a hitman to get you." )
if m:
    print( "Date {}; day {}; month {}; year {}".format( 
            m.group(0), m.group(1), m.group(2), m.group(3) ) )