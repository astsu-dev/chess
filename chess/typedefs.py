from typing import Literal, TypeVar

T = TypeVar("T")
Num = Literal[0, 1, 2, 3, 4, 5, 6, 7]
Letter = Literal["a", "b", "c", "d", "e", "f", "g", "h"]
LetterNum = Num
TermColor = Literal[
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white"
]
