from itertools import permutations, combinations
from random import randint, seed
from unittest import TestCase
import fib

seed(1010010001010101)


class Test(TestCase):
    def _test_invalid_input(self, func, test_params):
        with self.assertRaises(ValueError):
            func(*test_params)

    def _test_valid_input(self, func, test_params, expected_output):
        assert func(*test_params) == expected_output

    def test_kjfib_input(self):
        ### test invalid inputs
        for test_params in permutations(['0','-1','2.2']):
            yield self._test_invalid_input(fib.kjfib(), test_params)



    def test_fib(self):
        for test_params, expected in [(1,1),
                               (2,1),
                               (3,2),
                               (4,3),
                               (5,5)]:
            yield self._test_valid_input(fib.fib, test_params, expected)


    def test_kfib(self):
        for test_params, expected in [((1,2), 1),
                                      ((2, 2), 1),
                                      ((3, 2), 3),
                                      ((4, 2), 5),
                                      ((5, 2), 11),
                                      ((1, 3), 1),
                                      ((2, 3), 1),
                                      ((3, 3), 4),
                                      ((4, 3), 7),
                                      ((5, 3), 19),
                                      ]:
            yield self._test_valid_input(fib.fib, test_params, expected)


    def test_kjfib(self):

        ####
        # for n in [1,2] output is always 1
        random_kj_list = [randint(2,10) for i in range(5)]
        for k, j in permutations(random_kj_list, 2):
            yield self._test_valid_input(fib.kjfib, (1,k,j), 1)
            yield self._test_valid_input(fib.kjfib, (2,k,j), 1 )


        for test_params, expected in [((3, 2, 2), 1),
                                      ((4, 2, 2), 3),
                                      ((5, 2, 2), 5),
                                      ((3, 2, 3), 1),
                                      ((4, 2, 3), 1),
                                      ((5, 2, 3), 3),
                                      ((3, 3, 2), 1),
                                      ((4, 3, 2), 4),
                                      ((5, 3, 2), 7),
                                      ((3, 3, 3), 1),
                                      ((4, 3, 3), 1),
                                      ((5, 3, 3), 14),

                                      ]:
            yield self._test_valid_input(fib.fib, test_params, expected)