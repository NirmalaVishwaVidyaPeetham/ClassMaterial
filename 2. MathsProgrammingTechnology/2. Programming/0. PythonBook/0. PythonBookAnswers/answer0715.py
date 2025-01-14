PIRATES = 5
coconuts = 0
while True:
    coconuts += 1
    pile = coconuts
    for i in range( PIRATES ):
        if pile % PIRATES != 1:
            break
        pile = (PIRATES-1) * int( (pile - 1) / PIRATES )
    if pile % PIRATES == 1:
        break
print( coconuts )