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
    assert [cell.pos for cell in board.create_horizontal_roadmap(Position(x=5, y=3), Position(x=3, y=3))] == [
        Position(x=4, y=3),
        Position(x=3, y=3)
    ]
    assert [cell.pos for cell in board.create_horizontal_roadmap(Position(x=3, y=3), Position(x=6, y=3))] == [
        Position(x=4, y=3), Position(x=5, y=3),
        Position(x=6, y=3)
    ]


def test_create_vertical_roadmap(board):
    assert [cell.pos for cell in board.create_vertical_roadmap(Position(x=5, y=3), Position(x=5, y=6))] == [
        Position(x=5, y=4), Position(x=5, y=5),
        Position(x=5, y=6)
    ]
    assert [cell.pos for cell in board.create_vertical_roadmap(Position(x=5, y=3), Position(x=5, y=0))] == [
        Position(x=5, y=2), Position(x=5, y=1),
        Position(x=5, y=0)
    ]


def test_create_diagonal_roadmap(board):
    assert [cell.pos for cell in board.create_diagonal_roadmap(Position(x=3, y=3), Position(x=6, y=6))] == [
        Position(x=4, y=4), Position(x=5, y=5),
        Position(x=6, y=6)
    ]
    assert [cell.pos for cell in board.create_diagonal_roadmap(Position(x=2, y=3), Position(x=5, y=6))] == [
        Position(x=3, y=4), Position(x=4, y=5),
        Position(x=5, y=6)
    ]
    assert [cell.pos for cell in board.create_diagonal_roadmap(Position(x=3, y=3), Position(x=0, y=0))] == [
        Position(x=2, y=2), Position(x=1, y=1),
        Position(x=0, y=0)
    ]
    assert [cell.pos for cell in board.create_diagonal_roadmap(Position(x=2, y=3), Position(x=0, y=1))] == [
        Position(x=1, y=2),
        Position(x=0, y=1)
    ]


def test_create_knight_roadmap(board):
    assert [cell.pos for cell in board.create_knight_roadmap(Position(x=3, y=3), Position(x=1, y=4))] == [
        Position(x=1, y=4)
    ]


def test_create_roadmap(board):
    assert [cell.pos for cell in board.create_roadmap(Position(x=5, y=3), Position(x=3, y=3))] == [
        Position(x=4, y=3),
        Position(x=3, y=3)
    ]  # horizontal
    assert [cell.pos for cell in board.create_roadmap(Position(x=5, y=3), Position(x=5, y=6))] == [
        Position(x=5, y=4), Position(x=5, y=5),
        Position(x=5, y=6)
    ]  # vertical
    assert [cell.pos for cell in board.create_roadmap(Position(x=3, y=3), Position(x=6, y=6))] == [
        Position(x=4, y=4), Position(x=5, y=5),
        Position(x=6, y=6)
    ]  # diagonal
    assert [cell.pos for cell in board.create_roadmap(Position(x=3, y=3), Position(x=1, y=4))] == [
        Position(x=1, y=4)
    ]  # knight


def test_is_free_roadmap(board):
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert board.is_free_roadmap(roadmap[:-1])

    board = Board()
    board[3][4] = Knight(Color.BLACK, Position(x=4, y=3))
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert not board.is_free_roadmap(roadmap[:-1])

    board = Board()
    board[3][3] = Knight(Color.BLACK, Position(x=3, y=3))
    roadmap = board.create_horizontal_roadmap(
        Position(x=5, y=3), Position(x=3, y=3))
    assert board.is_free_roadmap(roadmap[:-1])
