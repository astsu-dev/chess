from .board import Board
from .enums import Color
from .game import Game


def main():
    board = Board()
    game = Game(board, Color.WHITE)
    game.start_game()
    game.print_pieces()
