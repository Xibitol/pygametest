from __future__ import annotations
from typing import Type, TypeVar, Optional, Iterable, Callable, Generic
import sys

class CLParser:
    """C-style command line options parser's class.

    This class parses you a string, like `sys.argv[1:]` the python script call's command line, and returns you
    each registered options' value (Booleans or Specifics) and other arguments. So, this class is an enhancement of the
    getopt.getopt() function.
    """

    # TODO: Methods:
    #     parse(string) -> Parses the 'string' or sys.argv[1:] and returns options' value and others arguments.

    def __init__(self) -> None:
        self._options: list[CLOption] = []

    # SETTERS
    def registerOption(self, option: CLOption):
        """Registers `option`, by copying it, to be recognized in the next `self.parse()` call.

        :raises SimilarOption: Thrown when you trying to register an option with the same id of another registered
            earlier.
        """

        # TODO: Check to raise SimilarOption error.
        self._options.append(option)

    # FUNCTIONS
    def parse(self):
        """"""
        raise NotImplementedError()

T = TypeVar("T")
class CLOption(Generic[T]):
    """"""

    def __init__(self, id: str, values: Optional[Type | T | Iterable[T]] = None, default: Optional[T] = None) -> None:
        # TODO: Doc; _values=None means "here or not", _values=Type means "whatever you want of type Type",
        # _values=T|Iterable[T] means an object of accepted values; _default=None means mandatory, _default=T means the
        # default value used.
        self._id = id
        self._values = values
        self._default = default

    # GETTERS
    @staticmethod
    def getPrefix() -> str:
        return "--"