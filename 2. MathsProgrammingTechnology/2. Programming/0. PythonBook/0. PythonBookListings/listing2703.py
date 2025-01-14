from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import exit

try:
    u = urlopen( "http://www.python.org" )
except HTTPError as e:
    print( "HTTP Error", e )
    sys.exit()
except URLError as e:
    print( "URL error", e )
    sys.exit()

for i in range( 5 ):
    text = u.readline()
    print( text )

u.close()