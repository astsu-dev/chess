from chess.enums import Color
from chess.position import Position
from chess.utils import (is_diagonal_path, is_horizontal_path,
                         is_vertical_path, reverse_color)


def test_is_horizontal_path():
    assert is_horizontal_path(Position(x=4, y=4), Position(x=2, y=4))
    assert is_horizontal_path(Position(x=4, y=4), Position(x=6, y=4))
    assert not is_horizontal_path(
        Position(x=4, y=4), Position(x=4, y=6))  # vertical
    assert not is_horizontal_path(
        Position(x=4, y=4), Position(x=4, y=2))  # vertical
    assert not is_horizontal_path(
        Position(x=4, y=4), Position(x=6, y=6))  # diagonal
    assert not is_horizontal_path(
        Position(x=4, y=4), Position(x=2, y=2))  # diagonal


def test_is_vertical_path():
    assert is_vertical_path(Position(x=4, y=4), Position(x=4, y=6))
    assert is_vertical_path(Position(x=4, y=4), Position(x=4, y=2))
    assert not is_vertical_path(
        Position(x=4, y=4), Position(x=2, y=4))  # horizontal
    assert not is_vertical_path(
        Position(x=4, y=4), Position(x=6, y=4))  # horizontal
    assert not is_vertical_path(
        Position(x=4, y=4), Position(x=6, y=6))  # diagonal
    assert not is_vertical_path(
        Position(x=4, y=4), Position(x=2, y=2))  # diagonal


def test_is_diagonal_path():
    assert is_diagonal_path(Position(x=4, y=4), Position(x=6, y=6))
    assert is_diagonal_path(Position(x=4, y=4), Position(x=2, y=2))
    assert not is_diagonal_path(
        Position(x=4, y=4), Position(x=2, y=4))  # horizontal
    assert not is_diagonal_path(
        Position(x=4, y=4), Position(x=6, y=4))  # horizontal
    assert not is_diagonal_path(
        Position(x=4, y=4), Position(x=4, y=6))  # vertical
    assert not is_diagonal_path(
        Position(x=4, y=4), Position(x=4, y=2))  # vertical


def test_reverse_color():
    assert reverse_color(Color.WHITE) is Color.BLACK
    assert reverse_color(Color.BLACK) is Color.WHITE
