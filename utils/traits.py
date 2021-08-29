from collections import Counter
from itertools import product
from config import *


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if (cls, kwargs['name']) not in cls._instances:
            cls._instances[(cls, kwargs['name'])] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[(cls, kwargs['name'])]


class Trait():
    def __init__(self, name):
        self.name = name
        self.alleles = (None,None)
        self._all_offspring_genotype_probabilities = {}
    @classmethod
    def genotype(clsm, allele_1, allele_2, name):
        if allele_1 and allele_2:
            return HomozygousDominant(name=name)
        elif allele_1 or allele_2:
            return Heterozygous(name=name)
        else:
            return HomozygousRecessive(name=name)

    def all_offspring_genotypes_probabilities(self, mate):
        possible_allele_combinations = product(self.alleles, mate.alleles)
        possible_genotypes = [self.genotype(*alleles, name = self.name) for alleles in possible_allele_combinations]
        possible_genotype_counts = Counter(possible_genotypes)
        total = len(possible_genotypes)
        self._all_offspring_genotype_probabilities[mate] = {genotype: (count / total) for genotype, count in possible_genotype_counts.items()}
        return self._all_offspring_genotype_probabilities[mate]

    def offspring_genotype_probability(self, mate_genotype, offspring_genotype):
        if mate_genotype not in self._all_offspring_genotype_probabilities:
            self.all_offspring_genotypes_probabilities(mate_genotype)
        return self._all_offspring_genotype_probabilities[mate_genotype][offspring_genotype]

class Heterozygous(Trait, metaclass=Singleton):

    def __init__(self, name):
        super().__init__(name)
        self.alleles = (True, False)


class HomozygousDominant(Trait, metaclass=Singleton):

    def __init__(self, name):
        super().__init__(name)
        self.alleles = (True, True)

class HomozygousRecessive(Trait, metaclass=Singleton):

    def __init__(self, name):
        super().__init__(name)
        self.alleles = (False, False)



