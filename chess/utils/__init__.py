from chess.enums import Color
from chess.position import Position
from chess.typedefs import Letter, LetterNum


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


def str_is_int(x: str) -> bool:
    """Returns True if str is int.

    Args:
        x (str)

    Returns:
        bool
    """

    try:
        int(x)
    except ValueError:
        return False
    return True


def convert_letter_to_letter_num(letter: Letter) -> LetterNum:
    """Converts `letter` to letter num.

    Args:
        letter (Letter)

    Returns:
        LetterNum: converted letter
    """

    d: dict[Letter, LetterNum] = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    return d[letter]


def convert_letter_num_to_letter(letter_num: LetterNum) -> Letter:
    """Converts `letter_num` to letter.

    Args:
        letter_num (LetterNum)

    Returns:
        Letter: converted `letter_num`
    """

    d: dict[LetterNum, Letter] = {
        0: "a", 
        1: "b", 
        2: "c", 
        3: "d", 
        4: "e", 
        5: "f", 
        6: "g", 
        7: "h",
    }
    return d[letter_num]
