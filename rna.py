from utils.utils import *

def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):
    dna_sequence = DNA(*read_n_sequences(input_dir / io_file, 1))

    rna_sequence = dna_sequence.transcribe_to_rna()

    write_output_file(output_dir / io_file, rna_sequence)


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')


