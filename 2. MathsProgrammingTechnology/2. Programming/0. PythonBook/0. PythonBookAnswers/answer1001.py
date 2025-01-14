text = """And Saint Attila raised the hand grenade up on high,
saying, "O Lord, bless this thy hand grenade, that with it
thou mayst blow thine enemies to tiny bits, in thy mercy." 
And the Lord did grin. And the people did feast upon the lambs, 
and sloths, and carp, and anchovies, and orangutans, and 
breakfast cereals, and fruit bats, and large chu..."""

counta, counte, counti, counto, countu = 0, 0, 0, 0, 0
for c in text:
    if c.upper() == "A":
        counta += 1
    elif c.upper() == "E":
        counte += 1
    elif c.upper() == "I":
        counti += 1
    elif c.upper() == "O":
        counto += 1
    elif c.upper() == "U":
        countu += 1
        
print( "Counts: a={}, e={}, i={}, o={}, u={}".format( 
    counta, counte, counti, counto, countu ) )