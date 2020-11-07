from chess.enums import Color
from chess.exceptions import UnpossibleMoveError
from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook
from chess.position import Position


def test_rook():
    piece = Rook(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=7, y=3))
    assert piece.can_move_to(Position(x=3, y=7))

    # Bishop
    assert not piece.can_move_to(Position(x=1, y=1))

    # Knight
    assert not piece.can_move_to(Position(x=4, y=5))
    assert not piece.can_move_to(Position(x=2, y=5))
    assert not piece.can_move_to(Position(x=4, y=1))
    assert not piece.can_move_to(Position(x=2, y=1))
    assert not piece.can_move_to(Position(x=1, y=2))
    assert not piece.can_move_to(Position(x=1, y=4))
    assert not piece.can_move_to(Position(x=5, y=2))
    assert not piece.can_move_to(Position(x=5, y=4))

    assert not piece.was_move
    piece.move_to(Position(x=5, y=3))
    assert piece.was_move


def test_knight():
    piece = Knight(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=4, y=5))
    assert piece.can_move_to(Position(x=2, y=5))
    assert piece.can_move_to(Position(x=4, y=1))
    assert piece.can_move_to(Position(x=2, y=1))
    assert piece.can_move_to(Position(x=1, y=2))
    assert piece.can_move_to(Position(x=1, y=4))
    assert piece.can_move_to(Position(x=5, y=2))
    assert piece.can_move_to(Position(x=5, y=4))

    # Bishop
    assert not piece.can_move_to(Position(x=2, y=2))

    # Rook
    assert not piece.can_move_to(Position(x=3, y=4))
    assert not piece.can_move_to(Position(x=2, y=3))


def test_bishop():
    piece = Bishop(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=2, y=2))
    assert piece.can_move_to(Position(x=4, y=4))
    assert piece.can_move_to(Position(x=2, y=4))

    # Rook
    assert not piece.can_move_to(Position(x=4, y=3))
    assert not piece.can_move_to(Position(x=3, y=2))

    # Knight
    assert not piece.can_move_to(Position(x=4, y=5))
    assert not piece.can_move_to(Position(x=2, y=5))
    assert not piece.can_move_to(Position(x=4, y=1))
    assert not piece.can_move_to(Position(x=2, y=1))
    assert not piece.can_move_to(Position(x=1, y=2))
    assert not piece.can_move_to(Position(x=1, y=4))
    assert not piece.can_move_to(Position(x=5, y=2))
    assert not piece.can_move_to(Position(x=5, y=4))


def test_queen():
    piece = Queen(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=7, y=3))
    assert piece.can_move_to(Position(x=3, y=7))
    assert piece.can_move_to(Position(x=2, y=2))
    assert piece.can_move_to(Position(x=4, y=4))
    assert piece.can_move_to(Position(x=1, y=5))

    # Knight
    assert not piece.can_move_to(Position(x=4, y=5))
    assert not piece.can_move_to(Position(x=2, y=5))
    assert not piece.can_move_to(Position(x=4, y=1))
    assert not piece.can_move_to(Position(x=2, y=1))
    assert not piece.can_move_to(Position(x=1, y=2))
    assert not piece.can_move_to(Position(x=1, y=4))
    assert not piece.can_move_to(Position(x=5, y=2))
    assert not piece.can_move_to(Position(x=5, y=4))


def test_king():
    piece = King(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=4, y=3))
    assert piece.can_move_to(Position(x=3, y=4))
    assert piece.can_move_to(Position(x=2, y=2))
    assert piece.can_move_to(Position(x=4, y=4))
    assert piece.can_move_to(Position(x=2, y=4))

    # Queen
    assert not piece.can_move_to(Position(x=7, y=3))
    assert not piece.can_move_to(Position(x=3, y=7))
    assert not piece.can_move_to(Position(x=1, y=1))
    assert not piece.can_move_to(Position(x=5, y=5))
    assert not piece.can_move_to(Position(x=1, y=5))

    # Knight
    assert not piece.can_move_to(Position(x=4, y=5))
    assert not piece.can_move_to(Position(x=2, y=5))
    assert not piece.can_move_to(Position(x=4, y=1))
    assert not piece.can_move_to(Position(x=2, y=1))
    assert not piece.can_move_to(Position(x=1, y=2))
    assert not piece.can_move_to(Position(x=1, y=4))
    assert not piece.can_move_to(Position(x=5, y=2))
    assert not piece.can_move_to(Position(x=5, y=4))

    assert not piece.was_move
    piece.move_to(Position(x=4, y=3))
    assert piece.was_move

    # Castling
    piece = King(Color.BLACK, Position(x=4, y=7))
    assert piece.can_move_to(Position(x=6, y=7))
    assert piece.can_move_to(Position(x=2, y=7))
    assert not piece.can_move_to(Position(x=7, y=7))
    assert not piece.can_move_to(Position(x=1, y=7))


def test_pawn():
    piece = Pawn(Color.WHITE, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=3, y=4))
    assert piece.can_move_to(Position(x=3, y=5))
    piece.move_to(Position(x=3, y=4))
    assert not piece.can_move_to(Position(x=3, y=6))

    piece = Pawn(Color.BLACK, Position(x=3, y=3))
    assert piece.can_move_to(Position(x=3, y=2))
    assert piece.can_move_to(Position(x=3, y=1))
    piece.move_to(Position(x=3, y=2))
    assert not piece.can_move_to(Position(x=3, y=0))

    # Knight
    assert not piece.can_move_to(Position(x=4, y=5))
    assert not piece.can_move_to(Position(x=2, y=5))
    assert not piece.can_move_to(Position(x=4, y=1))
    assert not piece.can_move_to(Position(x=2, y=1))
    assert not piece.can_move_to(Position(x=1, y=2))
    assert not piece.can_move_to(Position(x=1, y=4))
    assert not piece.can_move_to(Position(x=5, y=2))
    assert not piece.can_move_to(Position(x=5, y=4))

    # Queen
    assert not piece.can_move_to(Position(x=7, y=3))
    assert not piece.can_move_to(Position(x=3, y=7))
    assert not piece.can_move_to(Position(x=1, y=1))
    assert not piece.can_move_to(Position(x=5, y=5))
    assert not piece.can_move_to(Position(x=1, y=5))
