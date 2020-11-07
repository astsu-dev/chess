from .board import Board
from .cell import Cell
from .consts import letters_nums, nums
from .enums import Color
from .exceptions import InvalidColorError, NotPieceError, UnpossibleMoveError
from .pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook
from .position import Position
from .utils import reverse_color


class Game:
    def __init__(self, board: Board, color: Color) -> None:
        self._board = board
        self._color = color
        self._pieces: list[Piece] = []

    def start_game(self) -> None:
        """Starts new game."""

        self._arrange_pieces()
        self._current_move_color = Color.WHITE

    def move(self, from_: Position, to: Position) -> None:
        board = self._board
        cell = board[from_.y][from_.x]
        piece = cell.piece
        if piece is None:
            raise NotPieceError(cell)
        if piece.color is not self._current_move_color:
            raise InvalidColorError(self._current_move_color)
        if not piece.can_move_to(to):
            raise UnpossibleMoveError(piece, to)

        roadmap = board.create_roadmap(from_, to)
        is_free_roadmap = (board.is_free_roadmap(roadmap) if isinstance(
            piece, Pawn) else board.is_free_roadmap(roadmap[:-1]))
        if is_free_roadmap:
            piece.move_to(to)
            board[from_.y][from_.x].remove_piece()
            board[to.y][to.x].put_piece(piece)

        self._revert_color()

    def _revert_color(self) -> None:
        self._current_move_color = reverse_color(self._current_move_color)

    def print_pieces(self) -> None:
        for row in self._board:
            print("".join([str(cell) for cell in row]))

    def _arrange_pieces(self) -> None:
        """Arrange pieces on the board."""

        # Arrange pawns
        for letter_num in letters_nums:
            self._board[1][letter_num].put_piece(Pawn(
                Color.WHITE, Position(x=letter_num, y=1)))
        for letter_num in letters_nums:
            self._board[6][letter_num].put_piece(Pawn(
                Color.BLACK, Position(x=letter_num, y=6)))

        # Arrange rooks
        self._board[0][0].put_piece(Rook(Color.WHITE, Position(x=0, y=0)))
        self._board[0][7].put_piece(Rook(Color.WHITE, Position(x=7, y=0)))
        self._board[7][0].put_piece(Rook(Color.BLACK, Position(x=0, y=7)))
        self._board[7][7].put_piece(Rook(Color.BLACK, Position(x=7, y=7)))

        # Arrange knights
        self._board[0][1].put_piece(Knight(Color.WHITE, Position(x=1, y=0)))
        self._board[0][6].put_piece(Knight(Color.WHITE, Position(x=6, y=0)))
        self._board[7][1].put_piece(Knight(Color.BLACK, Position(x=1, y=7)))
        self._board[7][6].put_piece(Knight(Color.BLACK, Position(x=6, y=7)))

        # Arrange bishops
        self._board[0][2].put_piece(Bishop(Color.WHITE, Position(x=2, y=0)))
        self._board[0][5].put_piece(Bishop(Color.WHITE, Position(x=5, y=0)))
        self._board[7][2].put_piece(Bishop(Color.BLACK, Position(x=2, y=7)))
        self._board[7][5].put_piece(Bishop(Color.BLACK, Position(x=5, y=7)))

        # Arrange queens
        self._board[0][3].put_piece(Queen(Color.WHITE, Position(x=3, y=0)))
        self._board[7][3].put_piece(Queen(Color.BLACK, Position(x=3, y=7)))

        # Arrange kings
        self._board[0][4].put_piece(King(Color.WHITE, Position(x=4, y=0)))
        self._board[7][4].put_piece(King(Color.BLACK, Position(x=4, y=7)))

        for row in self._board:
            for cell in row:
                piece = cell.piece
                if piece is not None:
                    self._pieces.append(piece)
