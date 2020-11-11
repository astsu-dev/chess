import abc

from .enums import Color, Direction
from .move_path import MovePath
from .position import Position
from .utils import filter_by_valid_positions, only_from_range


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

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        return []


class HorizontalMoveRule(MoveRule):
    def __init__(self, max_move_length: int) -> None:
        self._max_move_length = max_move_length

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        max_move_length = self._max_move_length
        return from_.y == to.y and 0 < abs(to.x - from_.x) <= max_move_length

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

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
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        max_move_length = self._max_move_length
        return from_.x == to.x and 0 < abs(to.y - from_.y) <= max_move_length

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

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
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        max_move_length = self._max_move_length
        num_shift = abs(to.y - from_.y)
        letter_shift = abs(to.x - from_.x)
        return num_shift == letter_shift and 0 < num_shift <= max_move_length

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        fields = [
            *self._right_and_down_controlled_fields_from_position(pos),
            *self._left_and_down_controlled_fields_from_position(pos),
            *self._right_and_up_controlled_fields_from_position(pos),
            *self._left_and_up_controlled_fields_from_position(pos)
        ]

        return fields

    def _right_and_down_controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from in right and in down `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        max_move_length = self._max_move_length
        max_x_shift = abs(7 - pos.x)
        max_y_shift = abs(0 - pos.y)
        max_shift = min(
            max_move_length if max_x_shift > max_move_length else max_x_shift,
            max_move_length if max_y_shift > max_move_length else max_y_shift,
        )
        fields = [
            Position(x=x, y=y)
            for x, y in zip(range(pos.x + 1, pos.x + max_shift + 1), range(pos.y - 1, pos.y - max_shift - 1, -1))
        ]

        return fields

    def _left_and_down_controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from in left and in down `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        max_move_length = self._max_move_length
        max_x_shift = abs(0 - pos.x)
        max_y_shift = abs(0 - pos.y)
        max_shift = min(
            max_move_length if max_x_shift > max_move_length else max_x_shift,
            max_move_length if max_y_shift > max_move_length else max_y_shift,
        )
        fields = [
            Position(x=x, y=y)
            for x, y in zip(range(pos.x - 1, pos.x - max_shift - 1, -1), range(pos.y - 1, pos.y - max_shift - 1, -1))
        ]

        return fields

    def _right_and_up_controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from in right and in up `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        max_move_length = self._max_move_length
        max_x_shift = abs(7 - pos.x)
        max_y_shift = abs(7 - pos.y)
        max_shift = min(
            max_move_length if max_x_shift > max_move_length else max_x_shift,
            max_move_length if max_y_shift > max_move_length else max_y_shift,
        )
        fields = []
        fields = [
            Position(x=x, y=y)
            for x, y in zip(range(pos.x + 1, pos.x + max_shift + 1), range(pos.y + 1, pos.y + max_shift + 1))
        ]

        return fields

    def _left_and_up_controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from in left and in up `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        max_move_length = self._max_move_length
        max_x_shift = abs(0 - pos.x)
        max_y_shift = abs(7 - pos.y)
        max_shift = min(
            max_move_length if max_x_shift > max_move_length else max_x_shift,
            max_move_length if max_y_shift > max_move_length else max_y_shift,
        )
        fields = [
            Position(x=x, y=y)
            for x, y in zip(range(pos.x - 1, pos.x - max_shift - 1, -1), range(pos.y + 1, pos.y + max_shift + 1))
        ]

        return fields


class KnightMoveRule(MoveRule):
    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        y_shift = abs(to.y - from_.y)
        x_shift = abs(to.x - from_.x)
        return (x_shift == 1 and y_shift == 2) or (x_shift == 2 and y_shift == 1)

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        x_pos = pos.x
        y_pos = pos.y

        fields = [
            Position(x=x_pos + 2, y=y_pos + 1),
            Position(x=x_pos + 2, y=y_pos - 1),
            Position(x=x_pos - 2, y=y_pos + 1),
            Position(x=x_pos - 2, y=y_pos - 1),
            Position(x=x_pos + 1, y=y_pos + 2),
            Position(x=x_pos - 1, y=y_pos + 2),
            Position(x=x_pos + 1, y=y_pos - 2),
            Position(x=x_pos - 1, y=y_pos - 2)
        ]

        return filter_by_valid_positions(fields)


class PawnStraightMoveRule(MoveRule):
    def __init__(self, max_move_length: int, color: Color) -> None:
        self._max_move_length = max_move_length
        self._color = color

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        max_move_length = self._max_move_length
        color = self._color
        if color is Color.WHITE:
            return from_.x == to.x and 0 < to.y - from_.y <= max_move_length
        y_shift = to.y - from_.y
        return from_.x == to.x and y_shift < 0 and abs(y_shift) <= max_move_length

    @property
    def max_move_length(self) -> int:
        return self._max_move_length


class PawnBeatMoveRule(MoveRule):
    def __init__(self, color: Color) -> None:
        self._color = color

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        color = self._color
        y_shift = to.y - from_.y
        x_shift = abs(to.x - from_.x)
        if color is Color.WHITE:
            return y_shift > 0 and x_shift == y_shift and x_shift == 1
        return y_shift < 0 and x_shift == abs(y_shift) and x_shift == 1

    def controlled_fields_from_position(self, pos: Position) -> list[Position]:
        """Returns list of controled positions from `pos` position.

        Args:
            pos (Position)

        Returns:
            list[Position]
        """

        color = self._color
        if color is Color.BLACK:
            fields = [
                Position(x=pos.x - 1, y=pos.y - 1),
                Position(x=pos.x + 1, y=pos.y - 1),
            ]
        else:
            fields = [
                Position(x=pos.x - 1, y=pos.y + 1),
                Position(x=pos.x + 1, y=pos.y + 1),
            ]

        return filter_by_valid_positions(fields)


class CastlingMoveRule(MoveRule):
    def __init__(self, color: Color) -> None:
        self._color = color

    def is_valid_path(self, from_: Position, to: Position) -> bool:
        """Returns True if path is allowed by the rule.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            bool
        """

        color = self._color

        if color is Color.WHITE:
            return ((from_.x == 4 and from_.y == 0 and to.x == 6 and to.y == 0) or
                    (from_.x == 4 and from_.y == 0 and to.x == 2 and to.y == 0))
        else:
            return ((from_.x == 4 and from_.y == 7 and to.x == 6 and to.y == 7) or
                    (from_.x == 4 and from_.y == 7 and to.x == 2 and to.y == 7))
