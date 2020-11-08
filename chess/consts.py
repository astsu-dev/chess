from typing import Final, Literal

from .typedefs import Letter, LetterNum, Num, TermColor

BLACK_PIECE_COLOR: Final[TermColor] = "blue"
WHITE_PIECE_COLOR: Final[TermColor] = "cyan"

letters: Final[list[Letter]] = ["a", "b", "c", "d", "e", "f", "g", "h"]
letters_nums: Final[list[LetterNum]] = [0, 1, 2, 3, 4, 5, 6, 7]
nums: Final[list[Num]] = letters_nums
