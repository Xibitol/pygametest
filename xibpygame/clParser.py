from __future__ import annotations
from typing import TypeVar, Callable, Generic
import sys

class CLParser:
    """C-style command line options parser's class.

    This class parses you a string, like `sys.argv[1:]` the python script call's command line, and returns you
    each registered options' value (Booleans or Specifics) and other arguments. So, this class is an enhancement of the
    getopt.getopt() function.
    """
    # Methods:
    #     addOption(option) -> Adds an option by copying it.
    #     parse(string) -> Parses the 'string' or sys.argv[1:] and returns options value and others arguments.

    def __init__(self):
        self._options: list[CLOption] = []

    # SETTERS
    def registerOption(self, option: CLOption):
        """Registers `option`, by copying it, to be recognized in the next `self.parse()` call.

        :raises SimilarOption: Thrown when you trying to register an option with the same id of another registered
            earlier.
        """

        assert option != None, "What do you trying to give me ? A None value ..."

        # TODO: Check to raise SimilarOption error.
        self._options.append(option)

    # FUNCTIONS
    def parse(self):
        """"""
        pass

T = TypeVar("T")
class CLOption(Generic[T]):
    """"""

    def __init__(self):
        pass