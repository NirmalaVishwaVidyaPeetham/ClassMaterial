SIZE = 4

def solve_hanoi( pole_from, pole_tmp, pole_to, size ):
    if size == 1:
        print( "Disc 1 from", pole_from, "to", pole_to )
        return 1
    moves = solve_hanoi( pole_from, pole_to, pole_tmp, size-1 )
    print( "Disc", size, "from", pole_from, "to", pole_to )
    moves += 1+solve_hanoi( pole_tmp, pole_from, pole_to, size-1)
    return moves

moves = solve_hanoi( 'A', 'B', 'C', SIZE )
print( moves, "moves needed" )