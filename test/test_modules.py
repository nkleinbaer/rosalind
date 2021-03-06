import filecmp
from unittest import TestCase

import dna
import revc
import rna
import fib
import _gc
import hamm

from config import *


class Test(TestCase):
    def test_dna_main(self):
        io_file = f'rosalind_{Path(dna.__file__).stem}.txt'
        dna.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)

    def test_rna_main(self):
        io_file = f'rosalind_{Path(rna.__file__).stem}.txt'
        rna.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)

    def test_revc_main(self):
        io_file = f'rosalind_{Path(revc.__file__).stem}.txt'
        revc.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)

    def test_fib_main(self):
        io_file = f'rosalind_{Path(fib.__file__).stem}.txt'
        fib.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)

    def test_gc_main(self):
        io_file = f'rosalind{Path(_gc.__file__).stem}.txt'
        _gc.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)

    def test_hamm_main(self):
        io_file = f'rosalind_{Path(hamm.__file__).stem}.txt'
        hamm.main(io_file, TEST_DIR / 'input', TEST_DIR / 'output')
        assert filecmp.cmp(TEST_DIR / 'output' / io_file, TEST_DIR / 'output_check' / io_file)