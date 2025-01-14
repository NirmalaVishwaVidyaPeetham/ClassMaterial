class Fibo:
    def reset( self ):
        self.nr1 = 0
        self.nr2 = 1
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
        self.reset()
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.nr2 > self.maxnum:
            raise StopIteration()
        nr3 = self.nr1 + self.nr2
        self.nr1 = self.nr2
        self.nr2 = nr3
        return self.nr1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )