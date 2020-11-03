import abc

from .position import Position


class MoveRule(abc.ABC):
    @abc.abstractmethod
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        raise NotImplementedError


class VerticalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        return from_.x == to.x and 0 < abs(to.y - from_.y) <= max_move_length


class HorizontalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        return from_.y == to.y and 0 < abs(to.x - from_.x) <= max_move_length


class DiagonalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        num_shift = abs(to.y - from_.y)
        letter_shift = abs(to.x - from_.x)
        return num_shift == letter_shift and 0 < num_shift <= max_move_length


class KnightMoveRule(MoveRule):
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        y_shift = abs(to.y - from_.y)
        x_shift = abs(to.x - from_.x)
        return (x_shift == 1 and y_shift == 2) or (x_shift == 2 and y_shift == 1)


class PawnStraightMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        return from_.x == to.x and 0 < to.y - from_.y <= max_move_length

    @property
    def max_move_length(self) -> int:
        return self._max_move_length


class PawnBeatMoveRule(MoveRule):
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        y_shift = to.y - from_.y
        x_shift = abs(to.x - from_.x)
        return x_shift == y_shift and x_shift == 1


class CastlingMoveRule(MoveRule):
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        return ((from_.x == 4 and from_.y == 0 and to.x == 6 and to.y == 0) or
                (from_.x == 4 and from_.y == 0 and to.x == 2 and to.y == 0) or
                (from_.x == 4 and from_.y == 7 and to.x == 6 and to.y == 7) or
                (from_.x == 4 and from_.y == 7 and to.x == 2 and to.y == 7))
