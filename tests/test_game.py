import pytest
from chess.board import Board
from chess.enums import Color
from chess.game import Game


@pytest.fixture()
def game():
    board = Board()
    game = Game(board, Color.WHITE)
    game.start_game()
    return game


def test_revert_color(game):
    game.start_game()
    assert game._current_move_color is Color.WHITE
    game._revert_color()
    assert game._current_move_color is Color.BLACK
    game._revert_color()
    assert game._current_move_color is Color.WHITE
