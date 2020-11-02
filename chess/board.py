from typing import Union

from .cell import Cell
from .pieces import Piece
from .position import Position

BoardCell = Union[Piece, Cell]


class Board:
    def __init__(self) -> None:
        self._board: list[list[BoardCell]] = [
            [Cell(x=x, y=y) for x in range(8)] for y in range(8)
        ]

    def __getitem__(self, y: int) -> list[BoardCell]:
        return self._board[y]

    def is_free_roadmap(self, roadmap: list[BoardCell]) -> bool:
        """Returns True if roadmap don't have pieces.

        Args:
            roadmap (list[BoardCell])
        Returns:
            bool
        """

        return not bool([bc for bc in roadmap[:-1] if isinstance(bc, Piece)])

    def create_horizontal_roadmap(self, from_: Position, to: Position) -> list[BoardCell]:
        """Creates horizontal roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[BoardCell]: horizontal roadmap
        """

        x_shift = to.x - from_.x
        assert (x_shift > 0 or x_shift < 0), "unchecked path"
        x_step = 1 if x_shift > 0 else -1
        y = from_.y
        roadmap = [self._board[y][x]
                   for x in range(from_.x, to.x + x_step, x_step)]
        return roadmap[1:]

    def create_vertical_roadmap(self, from_: Position, to: Position) -> list[BoardCell]:
        """Creates vertical roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[BoardCell]: vertical roadmap
        """

        y_shift = to.y - from_.y
        assert (y_shift > 0 or y_shift < 0), "unchecked path"
        y_step = 1 if y_shift > 0 else -1
        x = from_.x
        roadmap = [self._board[y][x]
                   for y in range(from_.y, to.y + y_step, y_step)]
        return roadmap[1:]

    def create_diagonal_roadmap(self, from_: Position, to: Position) -> list[BoardCell]:
        """Creates diagonal roadmap to `to` positions.

        Args:
            from_ (Position): from position
            to (Position): to position

        Returns:
            list[BoardCell]: diagonal roadmap
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
