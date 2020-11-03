from typing import NamedTuple

from .position import Position


class MovePath(NamedTuple):
    from_: Position
    to: Position
