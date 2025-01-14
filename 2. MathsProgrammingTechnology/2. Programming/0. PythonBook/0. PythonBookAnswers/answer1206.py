from pcinput import getInteger

EMPTY = "-"
PLAYERX = "X"
PLAYERO = "O"
MAXMOVE = 9

def display_board( b ):
    print( "  1 2 3" )
    for row in range( 3 ):
        print( row+1, end=" ")
        for col in range( 3 ):
            print( b[row][col], end=" " )
        print()

def opponent( p ):
    if p == PLAYERX:
        return PLAYERO
    return PLAYERX
        
def getRowCol( player, what ):
    while True:
        num = getInteger( "Player "+player+", which "+what+
            " do you play? " )
        if num < 1 or num > 3:
            print( "Please enter 1, 2, or 3" )
            continue
        return num
    
def winner( b ):
    for row in range( 3 ):
        if b[row][0] != EMPTY and b[row][0] == b[row][1] \
            and b[row][0] == b[row][2]:
            return True
    for col in range( 3 ):
        if b[0][col] != EMPTY and b[0][col] == b[1][col] \
            and b[0][col] == b[2][col]:
            return True
    if b[1][1] != EMPTY:
        if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
            return True
        if b[1][1] == b[0][2] and b[1][1] == b[2][0]:
            return True
    return False

board = [[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY]]
player = PLAYERX

display_board( board )
move = 0
while True:
    row = getRowCol( player, "row" )
    col = getRowCol( player, "column" )
    if board[row-1][col-1] != EMPTY:
        print( "There is already a piece at row", row, 
            "and column", col )
        continue
    board[row-1][col-1] = player
    display_board( board )
    if winner( board ):
        print( "Player", player, "won!" )
        break
    move += 1
    if move == MAXMOVE:
        print( "It's a draw." )
        break
    player = opponent( player )