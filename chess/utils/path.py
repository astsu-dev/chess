from chess.enums import Color
from chess.position import Position
from chess.rules import (CastlingMoveRule, DiagonalMoveRule,
                         HorizontalMoveRule, KnightMoveRule, VerticalMoveRule)


def is_horizontal_path(from_: Position, to: Position) -> bool:
    """Returns True if path is horizontal.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return HorizontalMoveRule(7).is_valid_path(from_, to)


def is_vertical_path(from_: Position, to: Position) -> bool:
    """Returns True if path is vertical.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return VerticalMoveRule(7).is_valid_path(from_, to)


def is_diagonal_path(from_: Position, to: Position) -> bool:
    """Returns True if path is diagonal.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return DiagonalMoveRule(7).is_valid_path(from_, to)


def is_knight_path(from_: Position, to: Position) -> bool:
    """Returns True if path is knight.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return KnightMoveRule().is_valid_path(from_, to)


def is_castling_path(from_: Position, to: Position) -> bool:
    """Returns True if path is castling.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return (CastlingMoveRule(Color.WHITE).is_valid_path(from_, to) or
            CastlingMoveRule(Color.BLACK).is_valid_path(from_, to))
