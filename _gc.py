from utils.utils import *


def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):

    dna_collection = parse_fasta(input_dir / io_file, DNA)

    max_gc_sequence = max(dna_collection.keys(), key=(lambda seq_id: dna_collection[seq_id].gc_content))

    max_gc_content = '{:.6f}'.format(round(dna_collection[max_gc_sequence].gc_content * 100, 6))

    write_output_file(output_dir / io_file, [max_gc_sequence, max_gc_content])


if __name__ == '__main__':
    main(f'rosalind{Path(__file__).stem}.txt')
