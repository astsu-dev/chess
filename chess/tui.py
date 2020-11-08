import functools
import typing

from .board_printer import BoardPrinter
from .consts import letters, nums
from .exceptions import (ArgumentsCountError, CommandNotExistsError,
                         MovePathParseError)
from .game import Game
from .move_path import MovePath
from .position import Position
from .typedefs import Letter
from .utils import convert_letter_to_letter_num, str_is_int


class TUI:
    def __init__(self, game: Game, board_printer: BoardPrinter) -> None:
        self._game = game
        self._board_printer = board_printer
        self._commands = {
            "s": self._start_game,
            "start": self._start_game,
            "m": self._move,
            "move": self._move,
            "e": self._exit,
            "exit": self._exit,
            # "r": self._revert_board,
            # "reverse": self._revert_board
        }

    def run(self) -> None:
        self._game.start_game()
        while True:
            command = input("Command: ")
            self._handle_command(command)

    def _handle_command(self, command: str) -> None:
        """Handles string command, convert her to executor and execute him.

        Args:
            command (str)

        Raises:
            CommandNotExistsError: have will been raised if `command` not exists.
        """

        command = command.strip()

        if command:
            command_name, *args = command.split()
            try:
                command_executor = self._commands[command_name]
            except KeyError:
                raise CommandNotExistsError(command_name)
            
            command_executor(*args)

    def _move(self, *args: str) -> None:
        """Move command. Calls game move method.

        Raises:
            ArgumentsCountError: will have been raised if `args` length != 2
        """

        if len(args) != 2:
            raise ArgumentsCountError

        from_, to = args[0], args[1]
        path = self._parse_move_path(from_, to)

        self._game.move(path.from_, path.to)
        self._board_printer.print()
        self._print_current_move_color()

    def _start_game(self, *args: str) -> None:
        """Start game command. Calls game start_game method. Prints board."""

        self._game.start_game()
        self._board_printer.print()
        self._print_current_move_color()

    def _exit(self, *args: str) -> None:
        """Kill current process."""

        print("Bye!")
        exit(0)

    def _parse_move_path(self, from_: str, to: str) -> MovePath:
        """Parses user move input and returns MovePath.

        Args:
            move (str)

        Raises:
            MovePathParseError: will have been raised if path have invalid format.

        Returns:
            MovePath
        """

        if not self._is_valid_move_path_format(from_, to):
            raise MovePathParseError

        from_letter_num, from_num = (convert_letter_to_letter_num(
            typing.cast(Letter, from_[0])), int(from_[1]) - 1)
        to_letter_num, to_num = (convert_letter_to_letter_num(
            typing.cast(Letter, to[0])), int(to[1]) - 1)

        return MovePath(from_=Position(x=from_letter_num, y=from_num), to=Position(x=to_letter_num, y=to_num))

    def _is_valid_move_path_format(self, from_: str, to: str) -> bool:
        """Returns True if path have valid format.

        Args:
            from_ (str)
            to (str)

        Returns:
            bool
        """

        if len(from_) == 2 and len(to) == 2:
            from_x = from_[0]
            from_y = from_[1]
            to_x = to[0]
            to_y = to[1]
            if from_x in letters and to_x in letters:
                if str_is_int(from_y) and str_is_int(to_y):
                    input_nums = [n + 1 for n in nums]
                    if int(from_y) in input_nums and int(to_y) in input_nums:
                        return True
        return False

    def _print_current_move_color(self) -> None:
        print(self._game.current_move_color)

    # @staticmethod
    # def exception_handler(func) -> None:
    #     @functools.wraps(func)
    #     def wrapper(*args, **kwargs):
    #         return func(*args, **kwargs)
    #     return wrapper
