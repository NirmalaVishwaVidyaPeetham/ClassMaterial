import tkinter as tk
from time import sleep

class BrainvitaGUI:
    def __init__(self, master, initial_board):
        self.master = master
        master.title("Brainvita Solver")
        self.initial_board = [row[:] for row in initial_board] # Create a copy
        self.board_size = len(initial_board)
        self.cell_size = 60
        self.peg_radius = 20
        self.board_color = "lightgray"
        self.peg_color = "blue"
        self.empty_color = "white"
        self.move_delay = 0.5  # Seconds to wait between moves

        self.canvas = tk.Canvas(master, width=self.board_size * self.cell_size, height=self.board_size * self.board_size)
        self.canvas.pack()

        self.solution_window = tk.Toplevel(master)
        self.solution_window.title("Solution Steps")
        self.solution_text = tk.Text(self.solution_window, height=10, width=40)
        self.solution_text.pack()

        self.current_board = [row[:] for row in self.initial_board]
        self.solution_moves = []
        self.solving = False

        self.draw_board(self.current_board)

        solve_button = tk.Button(master, text="Solve", command=self.start_solving)
        solve_button.pack()

    def is_valid(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < len(self.current_board[0])

    def is_empty(self, row, col):
        return self.is_valid(row, col) and self.current_board[row][col] == '-'

    def is_peg(self, row, col):
        return self.is_valid(row, col) and self.current_board[row][col] == 'o'

    def get_possible_moves(self, board):
        moves = []
        n = len(board)
        for r in range(n):
            for c in range(len(board[r])):
                if board[r][c] == 'o':
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in directions:
                        jump_row, jump_col = r + dr, c + dc
                        land_row, land_col = r + 2 * dr, c + 2 * dc

                        if self.is_peg(jump_row, jump_col) and self.is_empty(land_row, land_col):
                            moves.append(((r, c), (land_row, land_col)))
        return moves

    def make_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        jumped_row, jumped_col = (start_row + end_row) // 2, (start_col + end_col) // 2

        board[start_row][start_col] = '-'
        board[jumped_row][jumped_col] = '-'
        board[end_row][end_col] = 'o'

    def unmake_move(self, board, start, end):
        start_row, start_col = start
        end_row, end_col = end
        jumped_row, jumped_col = (start_row + end_row) // 2, (start_col + end_col) // 2

        board[start_row][start_col] = 'o'
        board[jumped_row][jumped_col] = 'o'
        board[end_row][end_col] = '-'

    def solve_brainvita(self, board, moves_history):
        if sum(row.count('o') for row in board) == 1:
            self.solution_moves = list(moves_history)
            return True

        possible_moves = self.get_possible_moves(board)
        if not possible_moves:
            return False

        # Heuristic: Try moves that lead to fewer pegs first
        def score_move(move):
            start, end = move
            temp_board = [row[:] for row in board]
            self.make_move(temp_board, start, end)
            return sum(row.count('o') for row in temp_board)

        possible_moves.sort(key=score_move) # Sort moves by the number of remaining pegs

        for start, end in possible_moves:
            new_board = [row[:] for row in board]
            self.make_move(new_board, start, end)
            moves_history.append((start, end))
            if self.solve_brainvita(new_board, moves_history):
                return True
            moves_history.pop()

        return False

    def draw_board(self, board):
        self.canvas.delete("all")
        for r in range(self.board_size):
            for c in range(len(board[r])):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.board_color, outline="black")
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                if board[r][c] == 'o':
                    self.canvas.create_oval(center_x - self.peg_radius, center_y - self.peg_radius,
                                             center_x + self.peg_radius, center_y + self.peg_radius,
                                             fill=self.peg_color)
                elif board[r][c] == '-':
                    self.canvas.create_oval(center_x - self.peg_radius // 2, center_y - self.peg_radius // 2,
                                             center_x + self.peg_radius // 2, center_y + self.peg_radius // 2,
                                             fill=self.empty_color)

    def animate_solution(self):
        if not self.solution_moves:
            self.solution_text.insert(tk.END, "No solution found.\n")
            self.solving = False
            return

        if self.solution_moves:
            start, end = self.solution_moves.pop(0)
            start_row, start_col = start
            end_row, end_col = end
            jumped_row, jumped_col = (start_row + end_row) // 2, (start_col + end_col) // 2

            move_str = f"({start_row}, {start_col}) -> ({end_row}, {end_col})\n"
            self.solution_text.insert(tk.END, move_str)
            self.solution_text.see(tk.END) # Scroll to the latest move

            self.current_board[start_row][start_col] = '-'
            self.current_board[jumped_row][jumped_col] = '-'
            self.current_board[end_row][end_col] = 'o'
            self.draw_board(self.current_board)
            self.master.after(int(self.move_delay * 1000), self.animate_solution)
        else:
            self.solution_text.insert(tk.END, "Solution animation complete.\n")
            self.solving = False

    def start_solving(self):
        if not self.solving:
            self.solving = True
            self.solution_moves = []
            self.solution_text.delete(1.0, tk.END)
            current_board_copy = [row[:] for row in self.initial_board]
            if self.solve_brainvita(current_board_copy, []):
                self.solution_text.insert(tk.END, "Solution found. Animating moves...\n")
                self.current_board = [row[:] for row in self.initial_board]
                self.draw_board(self.current_board)
                self.master.after(int(self.move_delay * 1000), self.animate_solution)
            else:
                self.solution_text.insert(tk.END, "No solution found.\n")
                self.solving = False

# Initial Brainvita board configuration (English style)
initial_board = [
    ['-', '-', 'o', 'o', 'o', '-', '-'],
    ['-', '-', 'o', 'o', 'o', '-', '-'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', '-', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['-', '-', 'o', 'o', 'o', '-', '-'],
    ['-', '-', 'o', 'o', 'o', '-', '-']
]

if __name__ == "__main__":
    root = tk.Tk()
    gui = BrainvitaGUI(root, initial_board)
    root.mainloop()