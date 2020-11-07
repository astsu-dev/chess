from chess.enums import Color
from chess.position import Position


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


def filter_by_valid_positions(positions: list[Position]) -> list[Position]:
    """Returns list of positions with coords in 0 - 7 range.

    Args:
        positions (list[Position])

    Returns:
        list[Position]
    """

    return [pos for pos in positions if 0 <= pos.x < 8 and 0 <= pos.y < 8]
