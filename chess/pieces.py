import abc
from copy import deepcopy

from termcolor import colored

from .consts import BLACK_PIECE_COLOR, WHITE_PIECE_COLOR
from .enums import Color
from .position import Position
from .rules import (CastlingMoveRule, DiagonalMoveRule, HorizontalMoveRule,
                    KnightMoveRule, MoveRule, PawnBeatMoveRule,
                    PawnStraightMoveRule, VerticalMoveRule)


class Piece(abc.ABC):
    _rules: list[MoveRule]
    _white_char: str
    _black_char: str
    _name = "Piece"

    def __init__(self, color: Color, pos: Position) -> None:
        self._pos = pos
        self._color = color
        self._char = self._black_char if self._color is Color.BLACK else self._white_char
        self._rules = []

    @property
    def color(self) -> Color:
        return self._color

    @property
    def pos(self) -> Position:
        return self._pos

    def __str__(self) -> str:
        return self._char

    def __repr__(self) -> str:
        return f"{self._name}(color={self._color}, pos={self._pos})"

    def move_to(self, pos: Position) -> None:
        """Sets piece position to `pos`.

        Args:
            pos (Position): new position
        """

        self._pos = pos

    def can_move_to(self, pos: Position) -> bool:
        """Returns True if piece can move to `pos` by the her rules.

        Args:
            pos (Position)

        Returns:
            bool
        """

        return any((rule.is_valid_path(self._pos, pos) for rule in self._rules))

    def controlled_fields(self) -> list[Position]:
        """Returns list of controled positions by piece.

        Returns:
            list[Position]
        """

        fields = []
        for rule in self._rules:
            fields.extend(rule.controlled_fields_from_position(self._pos))
        return fields


class Rook(Piece):
    _name = "Rook"
    _white_char = colored("♖", WHITE_PIECE_COLOR)
    _black_char = colored("♜", BLACK_PIECE_COLOR)
    _white_char = colored("R", WHITE_PIECE_COLOR)
    _black_char = colored("R", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(7), VerticalMoveRule(7)]
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


class Knight(Piece):
    _name = "Knight"
    _white_char = colored("♘", WHITE_PIECE_COLOR)
    _black_char = colored("♞", BLACK_PIECE_COLOR)
    _white_char = colored("N", WHITE_PIECE_COLOR)
    _black_char = colored("N", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [KnightMoveRule()]


class Bishop(Piece):
    _name = "Bishop"
    _white_char = colored("♗", WHITE_PIECE_COLOR)
    _black_char = colored("♝", BLACK_PIECE_COLOR)
    _white_char = colored("B", WHITE_PIECE_COLOR)
    _black_char = colored("B", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [DiagonalMoveRule(7)]


class Queen(Piece):
    _name = "Queen"
    _white_char = colored("♕", WHITE_PIECE_COLOR)
    _black_char = colored("♛", BLACK_PIECE_COLOR)
    _white_char = colored("Q", WHITE_PIECE_COLOR)
    _black_char = colored("Q", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(7),
                       VerticalMoveRule(7), DiagonalMoveRule(7)]


class King(Piece):
    _name = "King"
    _white_char = colored("♔", WHITE_PIECE_COLOR)
    _black_char = colored("♚", BLACK_PIECE_COLOR)
    _white_char = colored("K", WHITE_PIECE_COLOR)
    _black_char = colored("K", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        self._rules = [HorizontalMoveRule(1),
                       VerticalMoveRule(1), DiagonalMoveRule(1), CastlingMoveRule(self._color)]
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
        if not self._was_move:
            self._remove_castling_move_rule()
            self._was_move = True

    def _remove_castling_move_rule(self) -> None:
        self._rules = [rule for rule in self._rules if not isinstance(
            rule, CastlingMoveRule)]


class Pawn(Piece):
    _name = "Pawn"
    _white_char = colored("♙", WHITE_PIECE_COLOR)
    _black_char = colored("♟", BLACK_PIECE_COLOR)
    _white_char = colored("P", WHITE_PIECE_COLOR)
    _black_char = colored("P", BLACK_PIECE_COLOR)

    def __init__(self, color: Color, pos: Position) -> None:
        super().__init__(color, pos)
        color = self._color
        self._rules = [PawnStraightMoveRule(1, color),
                       PawnStraightMoveRule(2, color), PawnBeatMoveRule(color)]
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
        if not self._was_move:
            self._remove_double_straight_move_rule()
            self._was_move = True

    def _remove_double_straight_move_rule(self) -> None:
        self._rules = [rule for rule in self._rules if isinstance(
            rule, PawnStraightMoveRule) and rule.max_move_length != 2]
