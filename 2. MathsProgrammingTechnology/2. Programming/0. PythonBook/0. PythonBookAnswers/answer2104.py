from copy import deepcopy

class FruitBasket:
    
    def __init__( self, fruits={} ):
        self.fruits = fruits
        
    def __repr__( self ):
        s = ""
        sep = "["
        for fruit in self.fruits:
            s += sep + fruit + ":" + str( self.fruits[fruit] )
            sep = ", "
        s += "]"
        return s
    
    def __contains__( self, fruit ):
        return fruit in self.fruits
    
    def __add__( self, fruit ):
        fbcopy = deepcopy( self )
        fbcopy.fruits[fruit] = fbcopy.fruits.get( fruit, 0 ) + 1
        return fbcopy
    
    def __iadd__( self, fruit ):
        self.fruits[fruit] = self.fruits.get( fruit, 0 ) + 1
        return self
    
    def __sub__( self, fruit ):
        if fruit not in self.fruits:
            return self
        fbcopy = deepcopy( self )
        fbcopy.fruits[fruit] = fbcopy.fruits.get( fruit, 0 ) - 1
        if fbcopy.fruits[fruit] <= 0:
            del fbcopy.fruits[fruit]
        return fbcopy
    
    def __isub__( self, fruit ):
        self.fruits[fruit] = self.fruits.get( fruit, 0 ) - 1
        if self.fruits[fruit] <= 0:
            del self.fruits[fruit]
        return self
    
    def __len__( self ):
        return len( self.fruits )
    
    def __getitem__( self, fruit ):
        return self.fruits.get( fruit, 0 )
    
    def __setitem__( self, fruit, n ):
        if n <= 0:
            if fruit in self.fruits:
                del self.fruits[fruit]
        else:
            self.fruits[fruit] = n
    
fb = FruitBasket()
fb += "apple"
fb += "apple"
fb += "banana"
fb = fb + "cherry"
fb["orange"] = 20
print( len( fb ) )
print( fb )
print( "banana" in fb )
print( "durian" in fb )
fb -= "apple"
fb -= "banana"
fb = fb - "cherry"
fb -= "durian"
print( fb )
print( "banana" in fb )
fb["orange"] = 0
print( fb )