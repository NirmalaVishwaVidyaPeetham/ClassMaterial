import re

pDate = re.compile(
    r"(?P<day>\d{1,2})-(?P<month>\d{1,2})-(?P<year>\d{4})")
m = pDate.search( "In response to your letter of 25-3-2015, \
I curse you." )
if m:
    print( "day is {}".format( m.group('day') ) )
    print( "month is {}".format( m.group('month') ) )
    print( "year is {}".format( m.group('year') ) )