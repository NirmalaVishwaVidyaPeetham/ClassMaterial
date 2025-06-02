import pygame
import sys


# Initialize PyGame
pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 24)
message_font = pygame.font.Font(None, 36)

# Constants
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 7, 7
SQUARE_SIZE = WIDTH // COLS
PEG_COLOR = (244, 0, 255)
EMPTY_COLOR = (192, 182, 192)
BOARD_COLOR = (0, 0, 0)
SELECTED_COLOR = (0, 0, 255)  # Color for selected peg
COUNTER = 32

board = None

# possible directions for valid moves (dx, dy)
directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BrainVita')


def init_board() -> None:
    global board, COUNTER, selected, running

    board = [
        [-1, -1, 1, 1, 1, -1, -1],
        [-1, -1, 1, 1, 1, -1, -1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [-1, -1, 1, 1, 1, -1, -1],
        [-1, -1, 1, 1, 1, -1, -1]
    ]

    COUNTER = 32
    update_counter()
    running = True
    selected = None
    draw_board()
    pygame.display.flip()


def update_counter()-> None:
    '''update the counter is dispaly on the screen'''
    text_surface = font.render(f"COUNTER = {COUNTER}", True, (255, 255, 255))  # Render the text using the font
    text_rect = text_surface.get_rect(center=(590, 20))
    screen.blit(text_surface, text_rect)


def prompt_message(message: str, duration=2000) -> None:  # Default duration is 2000 milliseconds (2 seconds)
    'print a message in the middle of the screen'
    print(message)
    message_surface = message_font.render(message, True, (0, 0, 0,), (255, 255, 255))  # Render the text using the font
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message_surface, message_rect)
    pygame.display.flip()  # Update the display
    pygame.time.wait(duration)  # Wait for the specified duration
    screen.fill((255, 255, 255))  # Clear the screen
    pygame.display.flip()  # Update the display


# Draw the board
def draw_board() -> None:
    '''draw the board game by the matrix'''
    screen.fill(BOARD_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != -1:
                color = PEG_COLOR if board[row][col] == 1 else EMPTY_COLOR
                if selected and selected == (row, col):
                    color = SELECTED_COLOR
                pygame.draw.circle(screen, color,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 10)

    pygame.draw.circle(screen, (0, 255, 0), (0 * SQUARE_SIZE + SQUARE_SIZE // 2, 0 * SQUARE_SIZE + SQUARE_SIZE // 2),
                       SQUARE_SIZE // 2 - 10)
    # Draw text on the circle
    text_surface = font.render("Reset", True, (0, 0, 0))  # Render the text using the font
    text_rect = text_surface.get_rect(center=(0 + 50, 0 + 45))
    screen.blit(text_surface, text_rect)
    update_counter()


def __print_board():
    for row in range(ROWS):
        for col in range(COLS):
            # print(board[row][col], end=' ')
            if board[row][col] == 1:
                print('X', end=' ')
            elif board[row][col] == 0:
                print('0', end=' ')
            else:
                print('.', end=' ')
        print()


def is_valid_move(x: int, y: int, dx:int , dy:int) -> bool:
    '''
    :param x: the x position of the selectio pin
    :param y: the y position of the selection pin
    :param dx: the x direction of the move from the selection pin (x- x_selected)
    :param dy: the y direction of the move from the selection pin (y - y_selected)
    :return: True if the move is valid, False otherwise
    '''
    if (dx, dy) not in directions:  # if is not a valid move by direction
        return False

    # check if the move is in the range of the board
    if not (0 <= x + dx < ROWS and 0 <= y + dy < COLS):
        return False

    # check if the selected pin is not empty
    # check if the middle pin is not empty, the  pin is going to be eaten
    # check if the new position is empty
    if board[x][y] == 1 and board[x + dx // 2][y + dy // 2] == 1 and board[x + dx][y + dy] == 0:
        return True
    return False


# Apply a move
def apply_move(x: int, y: int, dx: int, dy: int) -> None:
    board[x][y] = 0  # move the selected pin to the new position, remove from the old position
    board[x + dx // 2][y + dy // 2] = 0  # the middle position pin that has been eaten
    board[x + dx][y + dy] = 1  # set the new position pin to 1

    # update the counter
    global COUNTER
    COUNTER -= 1
    update_counter()
    __print_board()


def is_game_over() -> bool:
    if COUNTER > 1:
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    for direction in directions:
                        if is_valid_move(row, col, direction[0], direction[1]):
                            return True
    return False


def get_board_pos(x: int, y: int) -> (int, int):
    '''get the board position from the screen position, by dividing the screen position by the square size'''
    return y // SQUARE_SIZE, x // SQUARE_SIZE


def main():
    global running, selected, board, COUNTER
    # Initialize pygame
    init_board()
    while running:
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                row, col = get_board_pos(x, y)
                if (row, col) == (0, 0):
                    init_board()
                    continue

                if board[row][col] == 1:
                    selected = (row, col)
                elif selected:
                    dx = row - selected[0]
                    dy = col - selected[1]
                    if (dx, dy) in directions and is_valid_move(selected[0], selected[1], dx, dy):
                        apply_move(selected[0], selected[1], dx, dy)
                    selected = None

        pygame.display.flip()

        if not is_game_over():
            if COUNTER == 1:
                # Display the message
                prompt_message("WINNER WINNER CHICKEN DINNER!")
                init_board()
                continue

            prompt_message("Game Over")
            init_board()
            continue

from game import Game
import logging

if __name__ == '__main__':
    game = Game()
    game.run()
    # asyncio.run(main())
    # pygame.quit()
    # sys.exit()
