import abc

from .enums import Color, Direction
from .position import Position
from .utils import only_from_range


class MoveRule(abc.ABC):
    @abc.abstractmethod
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        raise NotImplementedError

    def create_controled_fields_map(self, pos: Position) -> list[Position]:
        """Returns list of positions which piece can beat.

        Args:
            pos (Position): piece position

        Returns:
            list[Position]
        """

        return []


class HorizontalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        return from_.y == to.y and 0 < abs(to.x - from_.x) <= max_move_length

    def controled_fields_from_position(self, pos: Position) -> list[Position]:
        max_move_length = self._max_move_length
        return [
            *[Position(x=x, y=pos.y) for x in range(only_from_range(pos.x -
                                                                    max_move_length, (0, pos.x)), pos.x)],
            *[Position(x=x, y=pos.y) for x in range(only_from_range(pos.x +
                                                                    max_move_length, (pos.x, 7)), pos.x, -1)],
        ]


class VerticalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        return from_.x == to.x and 0 < abs(to.y - from_.y) <= max_move_length

    def controled_fields_from_position(self, pos: Position) -> list[Position]:
        max_move_length = self._max_move_length
        return [
            *[Position(x=pos.x, y=y) for y in range(only_from_range(pos.y -
                                                                    max_move_length, (0, pos.y)), pos.y)],
            *[Position(x=pos.x, y=y) for y in range(only_from_range(pos.y +
                                                                    max_move_length, (pos.y, 7)), pos.y, -1)],
        ]


class DiagonalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        max_move_length = self._max_move_length
        num_shift = abs(to.y - from_.y)
        letter_shift = abs(to.x - from_.x)
        return num_shift == letter_shift and 0 < num_shift <= max_move_length

    def controled_fields_from_position(self, pos: Position) -> list[Position]:
        max_move_length = self._max_move_length
        fields = []

        # Right and down
        max_shift = min(
            (only_from_range(pos.x + max_move_length, (pos.x, 7))) - pos.x,
            (only_from_range(pos.y + max_move_length, (pos.y, 7))) - pos.y)
        fields.extend([Position(x=x, y=y) for x, y in zip(
            range(pos.x, pos.x + max_shift), range(pos.y, pos.y + max_shift))])

        # Left and down
        max_shift = min(
            (pos.x - only_from_range(pos.x - max_move_length, (0, pos.x))),
            (only_from_range(pos.y + max_move_length, (pos.y, 7))) - pos.y)
        fields.extend([Position(x=x, y=y) for x, y in zip(
            range(pos.x - max_shift, pos.x), range(pos.y, pos.y + max_shift))])

        # Right and up
        max_shift = min(
            (only_from_range(pos.x + max_move_length, (pos.x, 7))) - pos.x,
            (pos.y - only_from_range(pos.y - max_move_length, (0, pos.y))))
        fields.extend([Position(x=x, y=y) for x, y in zip(
            range(pos.x, pos.x + max_shift), range(pos.y - max_shift, pos.y))])

        # Left and up
        max_shift = min(
            (pos.x - only_from_range(pos.x - max_move_length, (0, pos.x))),
            (pos.y - only_from_range(pos.y - max_move_length, (0, pos.y))))
        fields.extend([Position(x=x, y=y) for x, y in zip(
            range(pos.x - max_shift, pos.x), range(pos.y - max_shift, pos.y))])

        return fields


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
    def __init__(self, color: Color) -> None:
        self._color = color

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        y_shift = to.y - from_.y
        x_shift = abs(to.x - from_.x)
        return x_shift == y_shift and x_shift == 1

    def controled_fields_from_position(self, pos: Position) -> list[Position]:
        color = self._color
        if color is Color.BLACK:
            return [
                Position(x=only_from_range(pos.x - 1, (0, pos.x)),
                         y=only_from_range(pos.y + 1, (0, pos.x))),
                Position(x=only_from_range(pos.x + 1, (pos.x, 7)),
                         y=only_from_range(pos.y + 1, (0, pos.x)))
            ]
        else:
            return [
                Position(x=only_from_range(pos.x - 1, (0, pos.x)),
                         y=only_from_range(pos.y - 1, (0, pos.x))),
                Position(x=only_from_range(pos.x + 1, (pos.x, 7)),
                         y=only_from_range(pos.y - 1, (0, pos.x)))
            ]


class CastlingMoveRule(MoveRule):
    def __init__(self, color: Color) -> None:
        self._color = color

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        color = self._color

        if color is Color.WHITE:
            return ((from_.x == 4 and from_.y == 0 and to.x == 6 and to.y == 0) or
                    (from_.x == 4 and from_.y == 0 and to.x == 2 and to.y == 0))
        else:
            return ((from_.x == 4 and from_.y == 7 and to.x == 6 and to.y == 7) or
                    (from_.x == 4 and from_.y == 7 and to.x == 2 and to.y == 7))
