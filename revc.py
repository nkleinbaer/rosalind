from utils.utils import *


def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):
    dna_sequence = DNA(*read_n_sequences(input_dir / io_file, 1))

    dna_sequence.get_reverse_compliment()

    write_output_file(output_dir / io_file, dna_sequence.reverse_compliment)


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')
