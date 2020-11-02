import abc

from .enums import Color
from .exceptions import UnpossibleMoveError
from .position import Position
from .rules import (CastlingMoveRule, DiagonalMoveRule, HorizontalMoveRule,
                    KnightMoveRule, MoveRule, PawnBeatMoveRule,
                    PawnStraightMoveRule, VerticalMoveRule)


class Piece(abc.ABC):
    _rules: list[MoveRule]
    _white_char: str
    _black_char: str
    _name: str

    def __init__(self, color: Color, pos: Position) -> None:
        self.pos = pos
        self._color = color
        self._char = self._black_char if self._color is Color.BLACK else self._white_char
        self._name = "Piece"
        self._rules = []

    @property
    def color(self) -> Color:
        return self._color

    def __str__(self) -> str:
        return self._char

    def __repr__(self) -> str:
        return f"{self._name}(color={self._color}, pos={self.pos})"

    def move_to(self, pos: Position) -> None:
        """Sets piece position to `pos`.

        Args:
            pos (Position): new position
        """

        if self.can_move_to(pos):
            self.pos = pos
        else:
            raise UnpossibleMoveError(f"piece can't move to {pos}")

    def can_move_to(self, pos: Position) -> bool:
        return any((rule.is_valid_path(self.pos, pos) for rule in self._rules))


class Rook(Piece):
    _white_char = "♖"
    _black_char = "♜"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(7), VerticalMoveRule(7)]


class Knight(Piece):
    _white_char = "♘"
    _black_char = "♞"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [KnightMoveRule()]


class Bishop(Piece):
    _white_char = "♗"
    _black_char = "♝"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [DiagonalMoveRule(7)]


class Queen(Piece):
    _white_char = "♕"
    _black_char = "♛"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(7),
                       VerticalMoveRule(7), DiagonalMoveRule(7)]


class King(Piece):
    _white_char = "♔"
    _black_char = "♚"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(1),
                       VerticalMoveRule(1), DiagonalMoveRule(1), CastlingMoveRule()]
        self._was_move = False

    @property
    def was_move(self) -> bool:
        return self._was_move

    def move_to(self, pos: Position) -> None:
        """Sets piece position to `pos`.

        Args:
            pos (Position): new position
        """

        super().move_to(pos)
        self._was_move = True


class Pawn(Piece):
    _white_char = "♙"
    _black_char = "♟"

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [PawnStraightMoveRule(1),
                       PawnStraightMoveRule(2), PawnBeatMoveRule()]

    def move_to(self, pos: Position) -> None:
        """Sets piece position to `pos`.

        Args:
            pos (Position): new position
        """

        self.old_pos = self.pos
        super().move_to(pos)
        if self.pos

    def _remove_double_straight_move_rule(self) -> None:
        self._rules = [rule for rule in self._rules if isinstance(
            rule, PawnStraightMoveRule) and rule.max_move_length != 2]
