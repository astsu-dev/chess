from chess.enums import Color
from chess.position import Position
from chess.utils import only_from_range, reverse_color
from chess.utils.path import (is_diagonal_path, is_horizontal_path,
                              is_knight_path, is_vertical_path)


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


def test_is_knight_path():
    assert is_knight_path(Position(x=3, y=3), Position(x=4, y=5))
    assert is_knight_path(Position(x=3, y=3), Position(x=2, y=5))
    assert is_knight_path(Position(x=3, y=3), Position(x=4, y=1))
    assert is_knight_path(Position(x=3, y=3), Position(x=2, y=1))
    assert is_knight_path(Position(x=3, y=3), Position(x=1, y=2))
    assert is_knight_path(Position(x=3, y=3), Position(x=1, y=4))
    assert is_knight_path(Position(x=3, y=3), Position(x=5, y=2))
    assert is_knight_path(Position(x=3, y=3), Position(x=5, y=4))
    assert not is_knight_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not is_knight_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not is_knight_path(
        Position(x=3, y=3), Position(x=4, y=6))  # length


def test_reverse_color():
    assert reverse_color(Color.WHITE) is Color.BLACK
    assert reverse_color(Color.BLACK) is Color.WHITE


def test_only_from_range():
    assert only_from_range(5, (1, 6)) == 5
    assert only_from_range(-2, (1, 6)) == 1
    assert only_from_range(7, (1, 6)) == 6
    assert only_from_range(6, (1, 6)) == 6
