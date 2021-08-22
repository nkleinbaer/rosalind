from typing import Dict

from utils.utils import *


def format_output(base_count_dict: Dict[str, int]) -> str:
    """

    Parameters
    ----------
    base_count_dict : Dict[str, int]
        A dictionary of base/count key-value pairs.

    Returns
    -------
    str
        A string with base counts formatted as specified by problem statement

    """
    return " ".join([f'{base_count_dict["A"]} '
                     f'{base_count_dict["C"]} '
                     f'{base_count_dict["G"]} '
                     f'{base_count_dict["T"]}'])


def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):
    dna_sequence = DNA(*read_n_sequences(input_dir / io_file, 1))

    base_count_dict = dna_sequence.count_bases()
    output_lines = format_output(base_count_dict)

    write_output_file(output_dir / io_file, output_lines)


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')
