allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera", 
    "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates","Plato","Eratosthenes","Cat","Dog"}

print( men.issubset( mortalthings ) ) # (a)
print( "Socrates" in men ) # (b)
print( "Socrates" in mortalthings ) # (c)
print( len( mortalthings.difference( men ) ) > 0 ) # (d)
print( len( allthings.difference( mortalthings ) ) > 0 ) # (e)