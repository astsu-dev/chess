from .board import Board
from .board_printer import BoardPrinter
from .enums import Color
from .game import Game
from .tui import TUI


def main():
    board = Board()
    game = Game(board, Color.WHITE)
    board_printer = BoardPrinter(board)
    tui = TUI(game, board_printer)
    tui.run()
