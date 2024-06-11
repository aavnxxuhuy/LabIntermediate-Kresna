import tkinter as tk
from tkinter import font, simpledialog
from typing import NamedTuple
from itertools import cycle


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = simpledialog.askinteger(
    title="Custom Board Tic Tac Toe yang T-nya 3",
    prompt="Masukkan angka antara 3 dan 6:",
    minvalue=3,
    maxvalue=6)
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="red"),
)


class TicTacToe_Game:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.win_combo = simpledialog.askinteger(
             title="Logika menang yang T-nya 3",
             prompt="Masukkan angka antara 3 dengan board size yang anda masukkan:",
             minvalue=3,
             maxvalue=board_size)
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        combos = []
        # Rows
        for row in range(self.board_size):
            for col in range(self.board_size - self.win_combo + 1):
                combo = [(row, col + i) for i in range(self.win_combo)]
                combos.append(combo)
        # Columns
        for col in range(self.board_size):
            for row in range(self.board_size - self.win_combo + 1):
                combo = [(row + i, col) for i in range(self.win_combo)]
                combos.append(combo)
        # Diagonals
        for row in range(self.board_size - self.win_combo + 1):
            for col in range(self.board_size - self.win_combo + 1):
                combo = [(row + i, col + i) for i in range(self.win_combo)]
                combos.append(combo)
        for row in range(self.win_combo - 1, self.board_size):
            for col in range(self.board_size - self.win_combo + 1):
                combo = [(row - i, col + i) for i in range(self.win_combo)]
                combos.append(combo)
        return combos

    def is_valid_move(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        """Process the current move and check if it's a win."""
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self._has_winner

    def is_tied(self):
        """Return True if the game is tied, and False otherwise."""
        no_winner = not self._has_winner
        played_moves = (move.label for row in self._current_moves for move in row)
        return no_winner and all(played_moves)

    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self._players)

    def reset_game(self):
        """Reset the game state to play again."""
        self._setup_board()
        self._has_winner = False
        self.winner_combo = []


class TicTacToe_Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Are You Ready Kidz?",
            font=font.Font(size=36, weight="bold"), )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=30)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=2,
                    height=1,
                    highlightbackground="lightblue",)
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

    def play(self, event):
        """Handle a player's move."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="green")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="yellow")

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def reset_board(self):
        """Reset the game's board to play again."""
        self._game.reset_game()
        self._update_display(msg="Are You Ready Kidz?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")


def main():
    game = TicTacToe_Game()
    board = TicTacToe_Board(game)
    board.mainloop()

if __name__ == "__main__":
    main()
