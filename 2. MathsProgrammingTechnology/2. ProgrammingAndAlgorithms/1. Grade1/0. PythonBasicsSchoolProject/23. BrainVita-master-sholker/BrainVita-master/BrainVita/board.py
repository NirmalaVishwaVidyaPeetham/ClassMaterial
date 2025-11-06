import pygame


class Board:
    ROWS = 7
    COLS = 7
    DIRECTIONS = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    PEG_COLOR = (244, 0, 255)
    EMPTY_COLOR = (192, 182, 192)
    BOARD_COLOR = (0, 0, 0)
    SELECTED_COLOR = (0, 0, 255)  # Color for selected peg

    def __init__(self, game):
        self.game = game
        self.board = [[]] # matrix
        self.counter = 0 # number of peg
        self.selected = None

        self.init_board()

    def init_board(self):
        self.board = [
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1]
        ]
        self.counter = 32
        self.update_counter()

    def update_counter(self):
        text_surface = self.game.font.render(f"COUNTER = {self.counter}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(590, 20))
        self.game.screen.blit(text_surface, text_rect)

    def draw_board(self):
        self.game.screen.fill((0, 0, 0))
        for row in range(7):
            for col in range(7):
                if self.board[row][col] != -1:
                    color = Board.PEG_COLOR if self.board[row][col] == 1 else (192, 182, 192)
                    if self.selected and self.selected == (row, col):
                        color = (Board.SELECTED_COLOR)
                    pygame.draw.circle(self.game.screen, color,
                                       (col * 100 + 50, row * 100 + 50), 40)
        # the reset button
        pygame.draw.circle(self.game.screen, (0, 255, 0),
                           (0 * self.game.SQUARE_SIZE + self.game.SQUARE_SIZE // 2, 0 * self.game.SQUARE_SIZE + self.game.SQUARE_SIZE // 2),
                           self.game.SQUARE_SIZE // 2 - 10)
        # Draw text on the circle
        text_surface = self.game.font.render("Reset", True, (0, 0, 0))  # Render the text using the font
        text_rect = text_surface.get_rect(center=(0 + 50, 0 + 45))
        self.game.screen.blit(text_surface, text_rect)
        self.update_counter()


    def set_selected(self, x: int, y: int) -> None:

        if self.selected and self.selected == (x, y):
            self.selected = None
        else:
            self.selected = (x, y)


    def is_valid_move(self, x: int, y: int, dx: int, dy: int) -> bool:
        if (dx, dy) not in Board.DIRECTIONS:
            return False

        if not (0 <= x + dx < Board.ROWS and 0 <= y + dy < Board.COLS):
            return False

        # check if there is a peg in the middle of the clicked position
        if (self.board[x][y] == 1 and self.board[x + dx // 2][y + dy // 2] == 1
                and self.board[x + dx][y + dy] == 0):
            return True
        return False


    def apply_move(self, x: int, y: int , dx: int, dy: int) -> None:
        self.board[x][y] = 0
        self.board[x + dx // 2][y + dy // 2] = 0
        self.board[x + dx][y + dy] = 1
        self.counter -= 1
        self.update_counter()
        self.selected = None


    def is_game_over(self) -> bool:
        '''check if there are any valid moves, if there is no valid move, the game is over'''
        if self.counter > 1:
            for row in range(Board.ROWS):
                for col in range(Board.COLS):
                    if self.board[row][col] == 1 and any(
                            self.is_valid_move(row, col, d[0], d[1]) for d in Board.DIRECTIONS):
                        return False
        return True
