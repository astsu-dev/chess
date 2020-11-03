import pytest
from chess.board import Board
from chess.cell import Cell
from chess.enums import Color
from chess.pieces import Knight
from chess.position import Position


@pytest.fixture()
def board():
    return Board()


def test_create_horizontal_roadmap(board):
    assert board.create_horizontal_roadmap(Position(x=5, y=3), Position(x=3, y=3)) == [
        Cell(x=4, y=3), Cell(x=3, y=3)
    ]
    assert board.create_horizontal_roadmap(Position(x=3, y=3), Position(x=6, y=3)) == [
        Cell(x=4, y=3), Cell(x=5, y=3), Cell(x=6, y=3)
    ]


def test_create_vertical_roadmap(board):
    assert board.create_vertical_roadmap(Position(x=5, y=3), Position(x=5, y=6)) == [
        Cell(x=5, y=4), Cell(x=5, y=5), Cell(x=5, y=6)
    ]
    assert board.create_vertical_roadmap(Position(x=5, y=3), Position(x=5, y=0)) == [
        Cell(x=5, y=2), Cell(x=5, y=1), Cell(x=5, y=0)
    ]


def test_create_diagonal_roadmap(board):
    assert board.create_diagonal_roadmap(Position(x=3, y=3), Position(x=6, y=6)) == [
        Cell(x=4, y=4), Cell(x=5, y=5), Cell(x=6, y=6)
    ]
    assert board.create_diagonal_roadmap(Position(x=2, y=3), Position(x=5, y=6)) == [
        Cell(x=3, y=4), Cell(x=4, y=5), Cell(x=5, y=6)
    ]
    assert board.create_diagonal_roadmap(Position(x=3, y=3), Position(x=0, y=0)) == [
        Cell(x=2, y=2), Cell(x=1, y=1), Cell(x=0, y=0)
    ]
    assert board.create_diagonal_roadmap(Position(x=2, y=3), Position(x=0, y=1)) == [
        Cell(x=1, y=2), Cell(x=0, y=1)
    ]


def test_create_knight_roadmap(board):
    assert board.create_knight_roadmap(Position(x=3, y=3), Position(x=1, y=4)) == [
        Cell(x=1, y=4)
    ]


def test_create_roadmap(board):
    assert board.create_roadmap(Position(x=5, y=3), Position(x=3, y=3)) == [
        Cell(x=4, y=3), Cell(x=3, y=3)
    ]  # horizontal
    assert board.create_roadmap(Position(x=5, y=3), Position(x=5, y=6)) == [
        Cell(x=5, y=4), Cell(x=5, y=5), Cell(x=5, y=6)
    ]  # vertical
    assert board.create_roadmap(Position(x=3, y=3), Position(x=6, y=6)) == [
        Cell(x=4, y=4), Cell(x=5, y=5), Cell(x=6, y=6)
    ]  # diagonal
    assert board.create_roadmap(Position(x=3, y=3), Position(x=1, y=4)) == [
        Cell(x=1, y=4)
    ]  # knight


def test_is_free_roadmap(board):
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert board.is_free_roadmap(roadmap)

    board = Board()
    board[3][4] = Knight(Color.BLACK, Position(x=4, y=3))
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert not board.is_free_roadmap(roadmap)

    board = Board()
    board[3][3] = Knight(Color.BLACK, Position(x=3, y=3))
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert board.is_free_roadmap(roadmap)
