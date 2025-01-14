from pcinput import getString
from random import randint

EMPTY = "."
BATTLESHIP = "X"
SHIPS = 3
WIDTH = 4
HEIGHT = 3

def displayBoard( b ):
    print( "  ", end="" )
    for col in range( WIDTH ):
        print( chr( ord("A")+col ), end=" " )
    print()
    for row in range( HEIGHT ):
        print( row+1, end=" ")
        for col in range( WIDTH ):
            print( b[row][col], end=" " )
        print()

def placeBattleships( b ):
    for i in range( SHIPS ):
        while True:
            x = randint( 0, WIDTH-1 )
            y = randint( 0, HEIGHT-1 )
            if b[y][x] == BATTLESHIP:
                continue
            if x > 0 and b[y][x-1] == BATTLESHIP:
                continue
            if x < WIDTH-1 and b[y][x+1] == BATTLESHIP:
                continue
            if y > 0 and b[y-1][x] == BATTLESHIP:
                continue
            if y < HEIGHT-1 and b[y+1][x] == BATTLESHIP:
                continue
            break
        b[y][x] = BATTLESHIP
    
def getTarget():
    while True:
        cell = getString( "Which cell do you target? " ).upper()
        if len( cell ) != 2:
            print( "Please enter a cell as XY,",
                "where X is a letter and Y a digit" )
            continue
        if cell[0] not in "ABCD":
            print( "The first character of the cell",
                "should be a letter in the range A-"+
                chr( ord("A")+WIDTH-1 ) )
            continue
        if cell[1] not in "123":
            print( "The second character of the cell should be",
                "a digit in the range 1-"+str( HEIGHT ) )
            continue
        return ord(cell[0])-ord("A"), ord(cell[1])-ord("1")      
    
board = []
for i in range( HEIGHT ):
    row = WIDTH * [EMPTY]
    board.append( row )
placeBattleships( board )
displayBoard( board )

hits = 0
moves = 0
while hits < SHIPS:
    x, y = getTarget()
    if board[y][x] == BATTLESHIP:
        print( "You sunk my battleship!" )
        board[y][x] = EMPTY
        hits += 1
    else:
        print( "Miss!" )
    moves += 1

print( "You needed", moves, "moves to sink all battleships." )