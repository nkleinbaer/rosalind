from unittest import TestCase

from utils.utils import *


class TestDNA(TestCase):

    def test__validate_base_set(self):
        with self.assertRaises(InvalidBaseError):
            DNA('x')

    def test__get_compliment(self):
        dna_sequence = DNA('GATACA')
        dna_sequence._get_compliment()
        assert dna_sequence.compliment == 'CTATGT'
