class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
        self.index = -1
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.index < len( self.seq )-1:
            self.index += 1
            return self.seq[self.index]
        raise StopIteration()
    def reset( self ):
        self.index = -1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )