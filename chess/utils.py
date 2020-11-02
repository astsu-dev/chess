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

    return from_.y == to.y and abs(to.x - from_.y) > 0


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


def reverse_color(color: Color) -> Color:
    """Returns reversed `color`

    Args:
        color (Color)

    Returns:
        Color
    """

    return Color.WHITE if color is Color.BLACK else Color.BLACK
