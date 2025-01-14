from datetime import datetime, timedelta

thisyear = datetime.now().year
xmasthisyear = datetime( thisyear, 12, 25, 23, 59, 59 )
thisday = datetime.now()
days = xmasthisyear - thisday

if days.days < 0:
    print( "Christmas will come again next year." )
elif days.days == 0:
    print( "It's Christmas!" )
else:
    print( "Only", days.days, "days to Christmas!" )