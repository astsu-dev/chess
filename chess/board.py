from copy import deepcopy
from typing import Iterator, Union

from .cell import Cell
from .consts import letters_nums, nums
from .controlled_cell import ControlledCell
from .enums import Color
from .exceptions import PathTypeError
from .pieces import Piece
from .position import Position
from .utils import convert_letter_num_to_letter
from .utils.path import (is_diagonal_path, is_horizontal_path, is_knight_path,
                         is_vertical_path)


class Board:
    def __init__(self) -> None:
        self._board: list[list[Cell]] = [
            [Cell(Position(x=x, y=y), (Color.WHITE if x % 2 == 0 else Color.BLACK) if y % 2 == 0 else (Color.BLACK if x % 2 == 0 else Color.WHITE))
                for x in letters_nums]
            for y in nums
        ]

    def __getitem__(self, y: int) -> list[Cell]:
        return self._board[y]

    def __iter__(self) -> Iterator[list[Cell]]:
        return iter(self._board)

    def __str__(self) -> str:
        board = self._board
        res = ""
        for num in nums:
            board_row = " ".join([str(c) for c in board[num]])
            res += f"{num + 1}  {board_row}\n"
        letters_row = " ".join(
            [convert_letter_num_to_letter(letter_num) for letter_num in letters_nums])
        res += f"\n   {letters_row}\n"
        return res

    def is_free_roadmap(self, roadmap: list[Cell]) -> bool:
        """Returns True if roadmap don't have pieces.

        Args:
            roadmap (list[Cell])
        Returns:
            bool
        """

        return not bool([bc for bc in roadmap if isinstance(bc, Piece)])

    def create_roadmap(self, from_: Position, to: Position) -> list[Cell]:
        """Creates roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[Cell]: roadmap
        """

        if is_horizontal_path(from_, to):
            return self.create_horizontal_roadmap(from_, to)
        if is_vertical_path(from_, to):
            return self.create_vertical_roadmap(from_, to)
        if is_diagonal_path(from_, to):
            return self.create_diagonal_roadmap(from_, to)
        if is_knight_path(from_, to):
            return self.create_knight_roadmap(from_, to)
        raise PathTypeError

    def create_horizontal_roadmap(self, from_: Position, to: Position) -> list[Cell]:
        """Creates horizontal roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[Cell]: horizontal roadmap
        """

        x_shift = to.x - from_.x
        assert (x_shift > 0 or x_shift < 0), "unchecked path"
        x_step = 1 if x_shift > 0 else -1
        y = from_.y
        roadmap = [self._board[y][x]
                   for x in range(from_.x, to.x + x_step, x_step)]
        return roadmap[1:]

    def create_vertical_roadmap(self, from_: Position, to: Position) -> list[Cell]:
        """Creates vertical roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[Cell]: vertical roadmap
        """

        y_shift = to.y - from_.y
        assert (y_shift > 0 or y_shift < 0), "unchecked path"
        y_step = 1 if y_shift > 0 else -1
        x = from_.x
        roadmap = [self._board[y][x]
                   for y in range(from_.y, to.y + y_step, y_step)]
        return roadmap[1:]

    def create_diagonal_roadmap(self, from_: Position, to: Position) -> list[Cell]:
        """Creates diagonal roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[Cell]: diagonal roadmap
        """

        x_shift = to.x - from_.x
        y_shift = to.y - from_.y
        assert (x_shift > 0 or x_shift < 0), "unchecked path"
        assert (y_shift > 0 or y_shift < 0), "unchecked path"

        y_step = 1 if y_shift > 0 else -1
        x_step = 1 if x_shift > 0 else -1

        roadmap = [self._board[y][x] for x, y in zip(
            range(from_.x, to.x + x_step, x_step), range(from_.y, to.y + y_step, y_step))]
        return roadmap[1:]

    def create_knight_roadmap(self, from_: Position, to: Position) -> list[Cell]:
        """Creates knight roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[Cell]: knight roadmap
        """

        return [self._board[to.y][to.x]]

    def get_pieces(self) -> list[Piece]:
        """Returns list of piece on the board.

        Returns:
            list[Piece]
        """

        pieces = [
            p for row in self._board for p in row if isinstance(p, Piece)]
        return pieces

    def pieces_controlled_cells(self) -> list[ControlledCell]:
        pieces = self.get_pieces()
        pieces_controlled_positions = [p.controlled_fields() for p in pieces]
        pieces_possible_paths = [p.controlled]
