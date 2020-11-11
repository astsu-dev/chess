import typing
from copy import deepcopy

from .board import Board
from .cell import Cell
from .consts import letters_nums, nums
from .controlled_cell import ControlledCell
from .enums import Color
from .exceptions import (CheckMate, HiddenCheckError, InvalidColorError,
                         NotPieceError, UnpossibleMoveError)
from .pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook
from .position import Position
from .utils import reverse_color


class Game:
    def __init__(self, board: Board, color: Color) -> None:
        self._board = board
        self._color = color
        self._pieces: list[Piece] = []
        self._current_move_color = Color.WHITE
        self._game_is_started = False

    @property
    def current_move_color(self) -> Color:
        return self._current_move_color

    @property
    def game_is_started(self) -> bool:
        return self._game_is_started

    def start_game(self) -> None:
        """Arranges pieces and set current move color to `Color.WHITE`."""

        self._arrange_pieces()
        self._current_move_color = Color.WHITE
        self._game_is_started = True

    def move(self, from_: Position, to: Position) -> None:
        """Move piece from `from_` to `to`.

        Args:
            from_ (Position)
            to (Position)

        Raises:
            NotPieceError: raised if board `from_` position cell not have piece.
            InvalidColorError: raised if piece from `from_` position have not current move color.
            UnpossibleMoveError: raised if piece can't move to `to` position.
            HiddenCheckError: raised if after move from `from_` to `to` king with current move color got check.
        """

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
            self.check_hidden_check(from_, to)
            board[from_.y][from_.x].remove_piece()
            board[to.y][to.x].put_piece(piece)
            piece.move_to(to)
        else:
            raise UnpossibleMoveError(piece, to)

        self._revert_color()

        self._check_checkmate(self._current_move_color)

    def _revert_color(self) -> None:
        """Change current move color to reverse color."""

        self._current_move_color = reverse_color(self._current_move_color)

    def _check_checkmate(self, color: Color) -> None:
        board = self._board
        pieces_controlled_cells = board.pieces_controlled_cells()
        friendly_pieces_controlled_cells = [
            cc for cc in pieces_controlled_cells if cc.piece.color is color]

        for controlled_cell in friendly_pieces_controlled_cells:
            piece_pos = controlled_cell.piece.pos
            future_board = deepcopy(board)
            future_piece = typing.cast(
                Piece, future_board[piece_pos.y][piece_pos.x].piece)
            future_board[piece_pos.y][piece_pos.x].remove_piece()
            future_board[controlled_cell.pos.y][controlled_cell.pos.x].put_piece(
                future_piece)
            future_piece.move_to(
                Position(x=controlled_cell.pos.x, y=controlled_cell.pos.y))
            future_pieces = future_board.get_pieces()
            future_pieces_controlled_cells = future_board.pieces_controlled_cells()
            king = self._get_king_from_pieces(future_pieces, color)
            if not self.piece_can_will_be_beaten(king, future_pieces_controlled_cells):
                return None
        raise CheckMate(color)

    def _get_king_from_pieces(self, pieces: list[Piece], color: Color) -> King:
        """Returns king with color as `color` from `pieces`.

        Args:
            pieces (list[Piece])
            color (Color)

        Returns:
            King
        """

        kings: list[King] = [p for p in pieces if isinstance(
            p, King) and p.color is color]

        return kings[0]

    def check_hidden_check(self, from_: Position, to: Position) -> None:
        """Raises HiddenCheckError if after move from `from_` to `to` king got check.

        Args:
            from_ (Position)
            to (Position)

        Raises:
            HiddenCheckError
        """

        future_board = deepcopy(self._board)
        future_piece = typing.cast(Piece, future_board[from_.y][from_.x].piece)
        future_board[from_.y][from_.x].remove_piece()
        future_board[to.y][to.x].put_piece(future_piece)
        future_piece.move_to(to)

        pieces = future_board.get_pieces()
        king = self._get_king_from_pieces(pieces, self._current_move_color)
        controlled_cells = future_board.pieces_controlled_cells()
        if self.piece_can_will_be_beaten(king, controlled_cells):
            raise HiddenCheckError

    def piece_can_will_be_beaten(self, piece: Piece, controlled_cells: list[ControlledCell]) -> bool:
        """Returns True if `piece` can will be beaten.

        Args:
            piece (Piece)
            controlled_cells (list[ControlledCell]): pieces controlled cells

        Returns:
            bool
        """

        piece_pos = piece.pos
        piece_color = piece.color
        for controlled_cell in controlled_cells:
            if controlled_cell.pos == piece_pos and controlled_cell.piece.color is not piece_color:
                return True
        return False

    def create_pieces_controlled_cells(self, pieces: list[Piece]) -> list[ControlledCell]:
        controlled_cells = []
        for piece in pieces:
            piece_controlled_fields = piece.controlled_fields()
            controlled_cells.extend(
                [ControlledCell(pos=f, piece=piece) for f in piece_controlled_fields])
        return controlled_cells

    def print_pieces(self) -> None:
        for row in self._board:
            print("".join([str(cell) for cell in row]))

    def _get_pieces_from_board(self, board: Board) -> list[Piece]:
        """Returns list of pieces from `board`.

        Args:
            board (Board)

        Returns:
            list[Piece]
        """

        pieces = []
        for row in self._board:
            for cell in row:
                piece = cell.piece
                if piece is not None:
                    pieces.append(piece)
        return pieces

    def _arrange_pieces(self) -> None:
        """Arrange pieces on the board."""

        board = self._board

        # Arrange pawns
        for letter_num in letters_nums:
            board[1][letter_num].put_piece(Pawn(
                Color.WHITE, Position(x=letter_num, y=1)))
        for letter_num in letters_nums:
            board[6][letter_num].put_piece(Pawn(
                Color.BLACK, Position(x=letter_num, y=6)))

        # Arrange rooks
        board[0][0].put_piece(Rook(Color.WHITE, Position(x=0, y=0)))
        board[0][7].put_piece(Rook(Color.WHITE, Position(x=7, y=0)))
        board[7][0].put_piece(Rook(Color.BLACK, Position(x=0, y=7)))
        board[7][7].put_piece(Rook(Color.BLACK, Position(x=7, y=7)))

        # Arrange knights
        board[0][1].put_piece(Knight(Color.WHITE, Position(x=1, y=0)))
        board[0][6].put_piece(Knight(Color.WHITE, Position(x=6, y=0)))
        board[7][1].put_piece(Knight(Color.BLACK, Position(x=1, y=7)))
        board[7][6].put_piece(Knight(Color.BLACK, Position(x=6, y=7)))

        # Arrange bishops
        board[0][2].put_piece(Bishop(Color.WHITE, Position(x=2, y=0)))
        board[0][5].put_piece(Bishop(Color.WHITE, Position(x=5, y=0)))
        board[7][2].put_piece(Bishop(Color.BLACK, Position(x=2, y=7)))
        board[7][5].put_piece(Bishop(Color.BLACK, Position(x=5, y=7)))

        # Arrange queens
        board[0][3].put_piece(Queen(Color.WHITE, Position(x=3, y=0)))
        board[7][3].put_piece(Queen(Color.BLACK, Position(x=3, y=7)))

        # Arrange kings
        board[0][4].put_piece(King(Color.WHITE, Position(x=4, y=0)))
        board[7][4].put_piece(King(Color.BLACK, Position(x=4, y=7)))
