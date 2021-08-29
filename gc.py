from utils.utils import *


def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):

    DNA_collection = parse_fasta(input_dir / io_file, DNA)

    max_gc_content = max(DNA_collection.keys(), key=(lambda seq_id: DNA_collection[seq_id].gc_content))

    write_output_file(output_dir / io_file, [max_gc_content, DNA_collection[max_gc_content].gc_content])


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')


