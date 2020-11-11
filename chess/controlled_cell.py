from typing import NamedTuple

from .pieces import Piece
from .position import Position


class ControlledCell(NamedTuple):
    pos: Position
    piece: Piece
