from random import randint, shuffle
from unittest import TestCase

from utils.utils import *


class TestNucleicAcid(TestCase):
    def test__get_compliment(self):
        random_base_counts = {base: randint(0, 250) for base in DNA_BASES}
        test_sequence = [base for base, count in random_base_counts.items() for i in range(count)]
        shuffle(test_sequence)
        test_sequence = NucleicAcid("".join(test_sequence))
        base_counts = test_sequence.count_bases()
        assert base_counts == random_base_counts


class TestDNA(TestCase):

    def test__validate_base_set(self):
        with self.assertRaises(InvalidBaseError):
            DNA('x')

    def test__get_compliment(self):
        dna_sequence = DNA('GATACA')
        dna_sequence._get_compliment()
        assert dna_sequence.compliment == 'CTATGT'

    def test__translate_to_rna(self):
        dna_sequence = DNA('GATACA')
        rna_sequence = dna_sequence.transcribe_to_rna()
        assert rna_sequence.sequence == RNA('GAUACA').sequence


class TestRNA(TestCase):
    def test__get_compliment(self):
        rna_sequence = RNA('GAUACA')
        rna_sequence._get_compliment()
        assert rna_sequence.compliment == 'CUAUGU'
