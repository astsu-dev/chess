from .board import Board


class BoardPrinter:
    """Class for printing board."""

    def __init__(self, board: Board) -> None:
        self._board = board

    def print(self) -> None:
        """Prints board."""

        print(self._board)
