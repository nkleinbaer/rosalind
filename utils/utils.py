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
        self.length = len(self.sequence)
        self.base_set = set(self.sequence)
        self._base_count_dict = None
        self._gc_content = None

    def _validate_base_set(self, valid_bases: Set[str]):
        if invalid_bases := self.base_set.difference(valid_bases):
            indexes = {base: [index for index in re.finditer(base, self.sequence)] for base in invalid_bases}
            raise InvalidBaseError(invalid_bases, indexes)

    def _get_compliment(self, compliments: Dict[str, str]):
        translation = self.sequence.maketrans(compliments)
        self.compliment = self.sequence.translate(translation)

    def get_reverse_compliment(self):
        self._get_compliment()
        self.reverse_compliment = self.compliment[::-1]

    @property
    def base_count(self) -> Dict[str, int]:
        if self._base_count_dict is None:
            self._base_count_dict = {}
            for base in self.sequence:
                self._base_count_dict[base] = self._base_count_dict.setdefault(base, 0) + 1

        return self._base_count_dict

    @property
    def gc_content(self) -> float:
        if self._gc_content is None:
            self._gc_content = (self.base_count['G'] + self.base_count['C']) / self.length
        return self._gc_content


class DNA(NucleicAcid):
    """
    Class for DNA sequences. Ensures all characters represent valid DNA nucleobases

    """

    def __init__(self, sequence: str):
        super().__init__(sequence)
        self._validate_base_set(DNA_BASES)

    def _get_compliment(self):
        super()._get_compliment(DNA_COMPLEMENTS)

    def transcribe_to_rna(self) -> 'RNA':
        return RNA(self.sequence.replace('T', 'U'))


class RNA(NucleicAcid):
    """
    Class for RNA sequence. Ensures all characters represent valid DNA nucleobases
    """

    def __init__(self, sequence: str):
        super().__init__(sequence)
        self._validate_base_set(RNA_BASES)

    def _get_compliment(self):
        super()._get_compliment(RNA_COMPLEMENTS)


def read_n_sequences(path: Union[Path, str], n: int = 1) -> Tuple[str]:
    """
    :param path: String or Path object pointing to an input file containing a genetic sequence on each line
    :param n: number of sequences to be returned
    :return:
    """
    with open(path, 'r') as f:
        line_list = f.read().splitlines()
    return tuple(line_list[:n])


def read_n_params(path: Union[Path, str], n: int = 1) -> Tuple[int]:
    """

    :param path: String or Path pointing to an input file containing whitespace delimited parameters
    :param n: number of params to return
    :return: a tuple of parameters
    """
    with open(path, 'r') as f:
        line = f.readline()
    return tuple([int(i) for i in line.split(" ")])


def write_output_file(path: str, data: Union[NucleicAcid, str, List[str]]) -> None:
    """
    Parameters
    ----------
    path : str
        Location to write output file.
    data : str | List[str]
        A NucleicAcid object, string or list of strings representing each line in the output text file.

    Returns
    -------
    None

    """
    if isinstance(data, NucleicAcid):
        data = data.sequence
    if not isinstance(data, List):
        data = [data]
    with open(path, 'w') as f:
        f.writelines([f'{line}\n' for line in data])


def parse_fasta(path: Union[Path, str], sequence_type: NucleicAcid = None) -> Dict[str, Union[str, NucleicAcid]]:
    with open(path, 'r') as f:
        line_list = f.read().splitlines()

    genetic_sequence_dict = {}
    for line in line_list:
        if line[0] == '>':
            sequence_id = line[1:]
            genetic_sequence_dict[sequence_id] = ""
        else:
            genetic_sequence_dict[sequence_id] += line.strip()

    if sequence_type:
        genetic_sequence_dict = {seq_id: sequence_type(seq) for seq_id, seq in genetic_sequence_dict.items()}
    return genetic_sequence_dict
