from utils.utils import *


def hamming_distance(s: str,t: str) -> int:
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    return distance

def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):
    sequence_1, sequence_2 = read_n_sequences(input_dir / io_file, 2, DNA)
    hamming_distance = sequence_1.hamming_distance(sequence_2)
    write_output_file(output_dir / io_file, hamming_distance)


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')