from pcinput import getInteger

class NotDividableBy:
    def __init__( self ):
        self.seq = list( range( 1, 101 ) )
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
    def process( self, num ):
        i = len( self.seq )-1
        while i >= 0:
            if self.seq[i]%num == 0:
                del self.seq[i]
            i -= 1
    def __len__( self ):
        return len( self.seq )

ndb = NotDividableBy()
while True:
    num = getInteger( "Give an integer: " )
    if num < 0:
        print( "Negative integers are ignored" )
        continue
    if num == 0:
        break
    ndb.process( num )

if len( ndb ) <= 0:
    print( "No numbers are left" )
else:
    for num in ndb:
        print( num, end=" " )