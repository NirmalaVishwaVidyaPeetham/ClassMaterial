from random import randint

deck = []
for value in ("Ace", "2", "3", "4", "5", "6", "7", "8", 
    "10", "Jack", "Queen", "King"):
    for suit in ("Hearts", "Spaces", "Clubs", "Diamonds"):
        deck.append( value + " of " + suit )
        
for i in range( len( deck ) ):
    j = randint( i, len( deck )-1 )
    deck[i], deck[j] = deck[j], deck[i]
    
for card in deck:
    print( card )