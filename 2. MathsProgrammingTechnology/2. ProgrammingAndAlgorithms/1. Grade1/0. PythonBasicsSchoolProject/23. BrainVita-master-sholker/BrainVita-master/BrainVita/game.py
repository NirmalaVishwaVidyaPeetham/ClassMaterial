import pygame
import sys
from board import Board

class Game:
    WIDTH, HEIGHT = 700, 700
    ROWS, COLS = 7, 7
    SQUARE_SIZE = WIDTH // COLS

    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        self.message_font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption('BrainVita')
        self.board = Board(self)
        self.running = True

    def get_board_pos(self, x: int, y:int ) -> int:
        return y // Game.SQUARE_SIZE, x // Game.SQUARE_SIZE

    def prompt_message(self, message, duration=2000):
        print(message)
        message_surface = self.message_font.render(message, True, (0, 0, 0), (255, 255, 255))
        message_rect = message_surface.get_rect(center=(Game.WIDTH // 2, Game.HEIGHT // 2))
        self.screen.blit(message_surface, message_rect)
        pygame.display.flip()
        pygame.time.wait(duration)
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)


    def handle_mouse_click(self, event):
        x, y = event.pos
        row, col = self.get_board_pos(x, y)
        if (row, col) == (0, 0):
            self.board = Board(self)
            return
        if self.board.board[row][col] == 1:
            self.board.set_selected(row, col)
            self.selected = (row, col)
        elif self.selected:
            dx = row - self.selected[0]
            dy = col - self.selected[1]
            if (dx, dy) in self.board.DIRECTIONS and self.board.is_valid_move(self.selected[0], self.selected[1], dx, dy):
                self.board.apply_move(self.selected[0], self.selected[1], dx, dy)
            self.selected = None


    def check_game_over(self):
        if self.board.is_game_over():
            if self.board.counter == 1:
                self.prompt_message("WINNER WINNER CHICKEN DINNER!")
            else:
                self.prompt_message("Game Over")
            self.board = Board(self)

    def run(self):
        self.board = Board(self)
        while self.running:
            self.board.draw_board()
            self.handle_events()
            pygame.display.flip()
            self.check_game_over()
