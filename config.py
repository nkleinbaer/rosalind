from pathlib import Path

INPUT_DIR = Path(r'C:\Users\nicho\PycharmProjects\rosalind\input')
OUTPUT_DIR = Path(r'C:\Users\nicho\PycharmProjects\rosalind\output')
TEST_DIR = Path(r'C:\Users\nicho\PycharmProjects\rosalind\test')

DNA_BASES = {'A', 'C', 'G', 'T'}
RNA_BASES = {'A', 'C', 'G', 'U'}
DNA_COMPLEMENTS = dict(A='T', C='G', G='C', T='A')
RNA_COMPLEMENTS = dict(A='U', C='G', G='C', U='A')
