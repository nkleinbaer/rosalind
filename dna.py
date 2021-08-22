from pathlib import Path
from typing import Dict, List

from utils.utils import *

def count_bases(s: NucleicAcid) -> Dict[str, int]:
    """
    Parameters
    ----------
    s : NucleicAcid
        An genetic sequence

    Returns
    -------
    Dict[str, int]
        A dictionary of each base and the # of times it occurs in s.

    """
    base_count_dict = {}
    for base in s.sequence:
        base_count_dict[base] = base_count_dict.setdefault(base, 0) + 1
        
    return base_count_dict


def format_output(base_count_dict: Dict[str, int]) -> List[str]:
    """

    Parameters
    ----------
    base_count_dict : Dict[str, int]
        A dictionary of base/count key-value pairs.

    Returns
    -------
    List[str]
        List of lines w/ output format as specified by problem.

    """
    return [f'{base_count_dict["A"]} ' \
            f'{base_count_dict["C"]} ' \
            f'{base_count_dict["G"]} ' \
            f'{base_count_dict["T"]}']
    
    
    
if __name__ == '__main__':
    io_file_name = f'rosalind_{Path(__file__).stem}.txt'
    dna_sequence = DNA(*read_n_sequences(INPUT_DIR/io_file_name, 1))

    base_count_dict = count_bases(dna_sequence)
    output_lines = format_output(base_count_dict)

    write_output_file(OUTPUT_DIR/io_file_name, output_lines)