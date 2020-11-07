from typing import Optional

from .enums import Color
from .pieces import Piece
from .position import Position


class Cell:
    """Board cell."""

    _white_char = "W"
    _black_char = "B"

    def __init__(self, pos: Position, color: Color) -> None:
        self._pos = pos
        self._color = color
        self._char = self._white_char if color is Color.WHITE else self._black_char
        self._piece: Optional[Piece] = None

    @property
    def pos(self) -> Position:
        return self._pos

    @property
    def color(self) -> Color:
        return self._color

    @property
    def piece(self) -> Optional[Piece]:
        return self._piece

    def __str__(self) -> str:
        piece = self._piece
        if piece is not None:
            return str(piece)
        return self._char

    def put_piece(self, piece: Piece) -> None:
        """Puts piece on cell.

        Args:
            piece (Piece)
        """

        self._piece = piece

    def remove_piece(self) -> None:
        """Remove piece from cell."""

        self._piece = None
