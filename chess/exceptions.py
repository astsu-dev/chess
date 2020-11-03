from .cell import Cell
from .enums import Color
from .pieces import Piece
from .position import Position


class UnpossibleMoveError(Exception):
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
    def __init__(self, cell: Cell) -> None:
        self._cell = cell

    @property
    def cell(self) -> Cell:
        return self._cell


class PathTypeError(Exception):
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
    def __init__(self, color: Color) -> None:
        self._color = color

    @property
    def color(self) -> Color:
        return self._color
