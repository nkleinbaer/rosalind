from random import randint, shuffle
from unittest import TestCase

from dna import count_bases
from utils.utils import *


class Test(TestCase):
    def test_count_bases(self):
        random_base_counts = {base: randint(0, 250) for base in DNA_BASES}
        test_sequence = [base for base, count in random_base_counts.items() for i in range(count)]
        shuffle(test_sequence)
        test_sequence = DNA("".join(test_sequence))
        base_counts = count_bases(test_sequence)
        assert base_counts == random_base_counts
