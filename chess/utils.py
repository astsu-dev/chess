from typing import Iterator

from .enums import Color
from .position import Position


def is_horizontal_path(from_: Position, to: Position) -> bool:
    """Returns True if path is horizontal.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return from_.y == to.y and abs(to.x - from_.x) > 0


def is_vertical_path(from_: Position, to: Position) -> bool:
    """Returns True if path is vertical.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return from_.x == to.x and abs(to.y - from_.y) > 0


def is_diagonal_path(from_: Position, to: Position) -> bool:
    """Returns True if path is diagonal.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    x_shift = abs(to.x - from_.x)
    y_shift = abs(to.y - from_.y)
    return x_shift == y_shift and x_shift > 0


def is_knight_path(from_: Position, to: Position) -> bool:
    """Returns True if path is knight.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    x_shift = abs(to.x - from_.x)
    y_shift = abs(to.y - from_.y)
    return (x_shift == 1 and y_shift == 2) or (x_shift == 2 and y_shift == 1)


def is_castling_path(from_: Position, to: Position) -> bool:
    """Returns True if path is castling.

    Args:
        from_ (Position): from position
        to (Position): to position
    Returns:
        bool
    """

    return ((from_.x == 4 and from_.y == 0 and to.x == 6 and to.y == 0) or
            (from_.x == 4 and from_.y == 0 and to.x == 2 and to.y == 0) or
            (from_.x == 4 and from_.y == 7 and to.x == 6 and to.y == 7) or
            (from_.x == 4 and from_.y == 7 and to.x == 2 and to.y == 7))


def reverse_color(color: Color) -> Color:
    """Returns reversed `color`

    Args:
        color (Color)

    Returns:
        Color
    """

    return Color.WHITE if color is Color.BLACK else Color.BLACK


def only_from_range(num: int, range_: tuple[int, int]) -> int:
    """
    Returns down range limit if `num` less than him.
    Returns up limit if `num` great than him.
    Otherwise returns `num`.

    Args:
        num (int)
        range_ (tuple[int, int]): 1 item - down limit, 2 item - up limit

    Returns:
        int
    """

    down_limit = range_[0]
    up_limit = range_[1]
    if num < down_limit:
        return down_limit
    if num > up_limit:
        return up_limit
    return num
