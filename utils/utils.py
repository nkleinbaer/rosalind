import re
from typing import List, Union, Set, Tuple, Dict

from config import *


class InvalidBaseError(Exception):
    """
    Exception raised when sequence contains an invalid character, i.e. a character not representing a valid nucelobase
    for a given type of genetic sequence

    Attributes:
        invalid_character -- the characters that caused the exceptions
        index -- the position of the invalid character in the string
        message -- explenation of the error
    """

    def __init__(self, invalid_characters, indexes):
        self.invalid_characters = invalid_characters
        self.message = f'Invalid character(s): "{invalid_characters} at positions {indexes}"'
        super().__init__(self.message)


class NucleicAcid:
    """
    Base class for all genetic sequences.

    Attributes:
        sequence -- genetic sequence as an uppercase string
        base_set -- set representing unique bases occuring in the sequence
    """

    def __init__(self, sequence: str):
        self.sequence = sequence.upper()
        self.base_set = set(self.sequence)

    def _validate_base_set(self, valid_bases: Set[str]):
        if invalid_bases := self.base_set.difference(valid_bases):
            indexes = {base: [index for index in re.finditer(base, self.sequence)] for base in invalid_bases}
            raise InvalidBaseError(invalid_bases, indexes)

    def _get_compliment(self, compliments: Dict[str, str]):
        translation = self.sequence.maketrans(compliments)
        self.compliment = self.sequence.translate(translation)


class DNA(NucleicAcid):
    """
    Class for DNA sequences. Ensures all characters represent valid DNA nucleobases

    """

    def __init__(self, sequence: str):
        super().__init__(sequence)
        self._validate_base_set(DNA_BASES)

    def _get_compliment(self):
        super()._get_compliment(DNA_COMPLEMENTS)


def read_n_sequences(path: Union[Path, str], n: int) -> Tuple[str]:
    """
    :param path: String or Path object pointing to an input file containing a genetic sequence on each line
    :param n: number of sequences to be returned
    :return:
    """
    with open(path, 'r') as f:
        line_list = f.read().splitlines()
    return tuple(line_list[:n])


def write_output_file(path: str, line_list: List[str]) -> None:
    """
    Parameters
    ----------
    path : str
        Location to write output file.
    line_list : List[str]
        A list of string representing each line in the output text file.

    Returns
    -------
    None

    """
    with open(path, 'w') as f:
        f.writelines([f'{line}\n' for line in line_list])
