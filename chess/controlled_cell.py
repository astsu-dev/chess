from typing import NamedTuple

from .enums import Color
from .position import Position


class ControlledCell(NamedTuple):
    pos: Position
    color: Color
