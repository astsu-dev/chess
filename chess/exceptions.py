from .cell import Cell
from .enums import Color
from .pieces import Piece
from .position import Position


class UnpossibleMoveError(Exception):
    """Raises if piece can't moves(because of rules) to `to` position."""

    def __init__(self, piece: Piece, to: Position) -> None:
        self._piece = piece
        self._to = to

    @property
    def piece(self) -> Piece:
        return self._piece

    @property
    def to(self) -> Position:
        return self._to


class NotPieceError(Exception):
    """Raises if player tried moved cell without piece."""

    def __init__(self, cell: Cell) -> None:
        self._cell = cell

    @property
    def cell(self) -> Cell:
        return self._cell


class PathTypeError(Exception):
    """Raises if path isn't diagonal, vertical, horizontal or knight."""

    def __init__(self, from_: Position, to: Position) -> None:
        self._from = from_
        self._to = to

    @property
    def from_(self) -> Position:
        return self._from

    @property
    def to(self) -> Position:
        return self._to


class InvalidColorError(Exception):
    """Raises if player moves piece not him color."""

    def __init__(self, color: Color) -> None:
        self._color = color

    @property
    def color(self) -> Color:
        return self._color


class HiddenCheckError(Exception):
    """Raises if player moved and after move him king got check."""


class MovePathParseError(Exception):
    """Raises if player input invalid move format."""


class ArgumentsCountError(Exception):
    """Raises if invalid command arguments count."""


class CommandNotExistsError(Exception):
    """Raises if command not exists."""

    def __init__(self, command_name: str) -> None:
        self._command_name = command_name

    @property
    def command_name(self) -> str:
        return self._command_name
