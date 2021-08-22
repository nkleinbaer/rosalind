from unittest import TestCase
import filecmp

from config import *
import dna


class Test(TestCase):
    def test_main(self):
        io_file = f'rosalind_{Path(dna.__file__).stem}.txt'
        dna.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)
