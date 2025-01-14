import re

pDate = re.compile( r"(\d{1,2})-(\d{1,2})-(\d{4})" )
datelist = pDate.findall( "In response to your letter of \
25-3-2015, on 27-3-2015 I decided to hire a hitman to get you." )
for date in datelist:
    print( date )