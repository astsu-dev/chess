from .board import Board
from .consts import letters_nums, nums
from .enums import Color
from .pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook
from .position import Position
from .utils import reverse_color


class Game:
    def __init__(self, board: Board, color: Color) -> None:
        self._board = board
        self._color = color

    def start_game(self) -> None:
        """Starts new game."""

        self._arrange_pieces()
        self._current_move_color = Color.WHITE

    def _arrange_pieces(self) -> None:
        """Arrange pieces on the board."""

        # Arrange pawns
        for letter_num in letters_nums:
            self._board[1][letter_num] = Pawn(
                Color.WHITE, Position(x=letter_num, y=1))
        for letter_num in letters_nums:
            self._board[6][letter_num] = Pawn(
                Color.BLACK, Position(x=letter_num, y=6))

        # Arrange rooks
        self._board[0][0] = Rook(Color.WHITE, Position(x=0, y=0))
        self._board[0][7] = Rook(Color.WHITE, Position(x=7, y=0))
        self._board[7][0] = Rook(Color.BLACK, Position(x=0, y=7))
        self._board[7][7] = Rook(Color.BLACK, Position(x=7, y=7))

        # Arrange knights
        self._board[0][1] = Knight(Color.WHITE, Position(x=1, y=0))
        self._board[0][6] = Knight(Color.WHITE, Position(x=6, y=0))
        self._board[7][1] = Knight(Color.BLACK, Position(x=1, y=7))
        self._board[7][6] = Knight(Color.BLACK, Position(x=6, y=7))

        # Arrange bishops
        self._board[0][2] = Bishop(Color.WHITE, Position(x=2, y=0))
        self._board[0][5] = Bishop(Color.WHITE, Position(x=5, y=0))
        self._board[7][2] = Bishop(Color.BLACK, Position(x=2, y=7))
        self._board[7][5] = Bishop(Color.BLACK, Position(x=5, y=7))

        # Arrange queens
        self._board[0][3] = Queen(Color.WHITE, Position(x=3, y=0))
        self._board[7][3] = Queen(Color.BLACK, Position(x=3, y=7))

        # Arrange kings
        self._board[0][4] = King(Color.WHITE, Position(x=4, y=0))
        self._board[7][4] = King(Color.BLACK, Position(x=4, y=7))
