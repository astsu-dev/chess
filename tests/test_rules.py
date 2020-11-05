from chess.position import Position
from chess.rules import (CastlingMoveRule, DiagonalMoveRule,
                         HorizontalMoveRule, KnightMoveRule, PawnBeatMoveRule,
                         PawnStraightMoveRule, VerticalMoveRule)


def test_horizontal_move_rule():
    rule = HorizontalMoveRule(7)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=0))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=0, y=3))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=10, y=0))  # length


def test_vertical_move_rule():
    rule = VerticalMoveRule(7)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=0, y=4))
    assert rule.is_valid_path(Position(x=3, y=2), Position(x=3, y=0))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=4))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=10))  # length


def test_diagonal_move_rule():
    rule = DiagonalMoveRule(7)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=3))
    assert rule.is_valid_path(Position(x=5, y=5), Position(x=4, y=6))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=2))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=0))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=10, y=10))  # length


def test_pawn_straight_move_rule():
    rule = PawnStraightMoveRule(1)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=0, y=1))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=2))  # length


def test_pawn_beat_move_rule():
    rule = PawnBeatMoveRule(Color.WHITE)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert rule.is_valid_path(Position(x=1, y=0), Position(x=0, y=1))
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=2, y=2))  # length


def test_knight_move_rule():
    rule = KnightMoveRule()
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=4, y=5))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=2, y=5))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=4, y=1))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=2, y=1))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=1, y=2))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=1, y=4))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=5, y=2))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=5, y=4))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=3, y=3), Position(x=4, y=6))  # length


def test_castling_move_rule():
    rule = CastlingMoveRule()
    assert rule.is_valid_path(Position(x=4, y=0), Position(x=2, y=0))
    assert rule.is_valid_path(Position(x=4, y=0), Position(x=6, y=0))
    assert rule.is_valid_path(Position(x=4, y=7), Position(x=2, y=7))
    assert rule.is_valid_path(Position(x=4, y=7), Position(x=6, y=7))
