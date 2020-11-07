from chess.enums import Color
from chess.position import Position
from chess.rules import (CastlingMoveRule, DiagonalMoveRule,
                         HorizontalMoveRule, KnightMoveRule, PawnBeatMoveRule,
                         PawnStraightMoveRule, VerticalMoveRule)


def test_horizontal_move_rule_is_valid_path():
    rule = HorizontalMoveRule(7)

    # is_valid_path
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=0))
    assert rule.is_valid_path(Position(x=3, y=3), Position(x=0, y=3))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=10, y=0))  # length


def test_horizontal_move_rule_controled_fields_from_position():
    rule = HorizontalMoveRule(7)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=0, y=4),
        Position(x=1, y=4),
        Position(x=2, y=4),
        Position(x=3, y=4),
        Position(x=7, y=4),
        Position(x=6, y=4),
        Position(x=5, y=4)
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=7, y=0),
        Position(x=6, y=0),
        Position(x=5, y=0),
        Position(x=4, y=0),
        Position(x=3, y=0),
        Position(x=2, y=0),
        Position(x=1, y=0)
    ]

    rule = HorizontalMoveRule(2)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=2, y=4),
        Position(x=3, y=4),
        Position(x=6, y=4),
        Position(x=5, y=4),
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=2, y=0),
        Position(x=1, y=0)
    ]


def test_vertical_move_rule_is_valid_path():
    rule = VerticalMoveRule(7)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=0, y=4))
    assert rule.is_valid_path(Position(x=3, y=2), Position(x=3, y=0))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=2, y=4))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=10))  # length


def test_vertical_move_rule_controled_fields_from_position():
    rule = VerticalMoveRule(7)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=4, y=0),
        Position(x=4, y=1),
        Position(x=4, y=2),
        Position(x=4, y=3),
        Position(x=4, y=7),
        Position(x=4, y=6),
        Position(x=4, y=5)
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=0, y=7),
        Position(x=0, y=6),
        Position(x=0, y=5),
        Position(x=0, y=4),
        Position(x=0, y=3),
        Position(x=0, y=2),
        Position(x=0, y=1)
    ]

    rule = VerticalMoveRule(2)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=4, y=2),
        Position(x=4, y=3),
        Position(x=4, y=6),
        Position(x=4, y=5)
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=0, y=2),
        Position(x=0, y=1)
    ]


def test_diagonal_move_rule_is_valid_path():
    rule = DiagonalMoveRule(7)
    assert rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=3))
    assert rule.is_valid_path(Position(x=5, y=5), Position(x=4, y=6))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=2))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=3, y=0))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=10, y=10))  # length


def test_diagonal_move_rule_controled_fields_from_position():
    rule = DiagonalMoveRule(7)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=5, y=3),
        Position(x=6, y=2),
        Position(x=7, y=1),

        Position(x=3, y=3),
        Position(x=2, y=2),
        Position(x=1, y=1),
        Position(x=0, y=0),

        Position(x=5, y=5),
        Position(x=6, y=6),
        Position(x=7, y=7),

        Position(x=3, y=5),
        Position(x=2, y=6),
        Position(x=1, y=7)
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=1, y=1),
        Position(x=2, y=2),
        Position(x=3, y=3),
        Position(x=4, y=4),
        Position(x=5, y=5),
        Position(x=6, y=6),
        Position(x=7, y=7)
    ]

    rule = DiagonalMoveRule(2)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=5, y=3),
        Position(x=6, y=2),

        Position(x=3, y=3),
        Position(x=2, y=2),

        Position(x=5, y=5),
        Position(x=6, y=6),

        Position(x=3, y=5),
        Position(x=2, y=6)
    ]
    assert rule.controled_fields_from_position(Position(x=0, y=0)) == [
        Position(x=1, y=1),
        Position(x=2, y=2)
    ]


def test_knight_move_rule_is_valid_path():
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


def test_knight_move_rule_controled_fields_from_position():
    rule = KnightMoveRule()
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=6, y=5),
        Position(x=6, y=3),

        Position(x=2, y=5),
        Position(x=2, y=3),

        Position(x=5, y=6),
        Position(x=3, y=6),

        Position(x=5, y=2),
        Position(x=3, y=2)
    ]

    assert rule.controled_fields_from_position(Position(x=1, y=1)) == [
        Position(x=3, y=2),
        Position(x=3, y=0),

        Position(x=2, y=3),
        Position(x=0, y=3)
    ]


def test_pawn_straight_move_rule_is_valid_path():
    rule = PawnStraightMoveRule(1, Color.WHITE)
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=4, y=5))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=4, y=3))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=2))  # length

    rule = PawnStraightMoveRule(1, Color.BLACK)
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=4, y=3))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=4, y=5))
    assert not rule.is_valid_path(Position(x=0, y=0), Position(x=1, y=1))
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=2))  # length


def test_pawn_straight_move_rule_controled_fields_from_position():
    rule = PawnStraightMoveRule(1, Color.WHITE)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == []
    rule = PawnStraightMoveRule(1, Color.BLACK)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == []


def test_pawn_beat_move_rule_is_valid_path():
    rule = PawnBeatMoveRule(Color.WHITE)
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=5, y=5))
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=3, y=5))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=3, y=3))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=5, y=3))

    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=2, y=2))  # length

    rule = PawnBeatMoveRule(Color.BLACK)
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=3, y=3))
    assert rule.is_valid_path(Position(x=4, y=4), Position(x=5, y=3))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=5, y=5))
    assert not rule.is_valid_path(Position(x=4, y=4), Position(x=3, y=5))

    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=0, y=0))  # not move
    assert not rule.is_valid_path(
        Position(x=0, y=0), Position(x=2, y=2))  # length


def test_pawn_beat_move_rule_controled_fields_from_position():
    rule = PawnBeatMoveRule(Color.WHITE)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=3, y=5), Position(x=5, y=5)]
    assert rule.controled_fields_from_position(
        Position(x=0, y=0)) == [Position(x=1, y=1)]
    assert rule.controled_fields_from_position(Position(x=4, y=7)) == []
    assert not rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=3, y=3), Position(x=5, y=3)]
    assert not rule.controled_fields_from_position(
        Position(x=7, y=7)) == [Position(x=6, y=6)]
    assert not rule.controled_fields_from_position(Position(x=4, y=0)) == []

    rule = PawnBeatMoveRule(Color.BLACK)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=3, y=3), Position(x=5, y=3)]
    assert rule.controled_fields_from_position(
        Position(x=7, y=7)) == [Position(x=6, y=6)]
    assert rule.controled_fields_from_position(Position(x=4, y=0)) == []
    assert not rule.controled_fields_from_position(Position(x=4, y=4)) == [
        Position(x=3, y=5), Position(x=5, y=5)]
    assert not rule.controled_fields_from_position(
        Position(x=0, y=0)) == [Position(x=1, y=1)]
    assert not rule.controled_fields_from_position(Position(x=4, y=7)) == []


def test_castling_move_rule_is_valid_path():
    rule = CastlingMoveRule(Color.WHITE)
    assert rule.is_valid_path(Position(x=4, y=0), Position(x=2, y=0))
    assert rule.is_valid_path(Position(x=4, y=0), Position(x=6, y=0))
    assert not rule.is_valid_path(Position(x=4, y=7), Position(x=2, y=7))
    assert not rule.is_valid_path(Position(x=4, y=7), Position(x=6, y=7))

    rule = CastlingMoveRule(Color.BLACK)
    assert not rule.is_valid_path(Position(x=4, y=0), Position(x=2, y=0))
    assert not rule.is_valid_path(Position(x=4, y=0), Position(x=6, y=0))
    assert rule.is_valid_path(Position(x=4, y=7), Position(x=2, y=7))
    assert rule.is_valid_path(Position(x=4, y=7), Position(x=6, y=7))


def test_castling_move_rule_controled_fields_from_position():
    rule = CastlingMoveRule(Color.WHITE)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == []
    rule = CastlingMoveRule(Color.BLACK)
    assert rule.controled_fields_from_position(Position(x=4, y=4)) == []
