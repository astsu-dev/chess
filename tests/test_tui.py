import pytest
from chess.board import Board
from chess.board_printer import BoardPrinter
from chess.enums import Color
from chess.exceptions import MovePathParseError
from chess.game import Game
from chess.move_path import MovePath
from chess.position import Position
from chess.tui import TUI


@pytest.fixture()
def tui():
    board = Board()
    game = Game(board, Color.WHITE)
    board_printer = BoardPrinter(board)
    return TUI(game, board_printer)


def test_is_valid_move_path_format(tui):
    assert tui._is_valid_move_path_format("a8", "b2")
    assert tui._is_valid_move_path_format("a8", "b8")
    assert not tui._is_valid_move_path_format("a9", "b2")
    assert not tui._is_valid_move_path_format("a9", "b9")
    assert not tui._is_valid_move_path_format("u8", "b2")
    assert not tui._is_valid_move_path_format("u8", "q2")


def test_parse_move_path(tui):
    assert tui._parse_move_path("a8", "b2") == MovePath(
        Position(x=0, y=7), Position(x=1, y=1))
    assert tui._parse_move_path("a8", "b8") == MovePath(
        Position(x=0, y=7), Position(x=1, y=7))
    try:
        tui._parse_move_path("a9", "b2")
    except MovePathParseError:
        ...
    else:
        assert False
    try:
        tui._parse_move_path("a9", "b9")
    except MovePathParseError:
        ...
    else:
        assert False
    try:
        tui._parse_move_path("u8", "b2")
    except MovePathParseError:
        ...
    else:
        assert False
    try:
        tui._parse_move_path("u8", "q2")
    except MovePathParseError:
        ...
    else:
        assert False
