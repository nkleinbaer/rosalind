from functools import lru_cache
from utils.utils import *


def _validate_kjfib_input(**kwargs):
    for kw, arg in kwargs.items():
        if not isinstance(arg, int) or arg < 1:
            raise ValueError


@lru_cache()
def kjfib(n: int, k: int, j: int) -> int:
    _validate_kjfib_input(n=n, k=k, j=j)

    if n <= 2:
        return 1
    else:
        return kfib(n - 1, k) + k * kfib(n - j, k)


def kfib(n: int, k: int) -> int:
    return kjfib(n, k, 2)


def fib(n: int) -> int:
    return kfib(n, 1)


def main(io_file, input_dir: Path = INPUT_DIR, output_dir: Path = OUTPUT_DIR):
    n, k = read_n_params(input_dir / io_file, 2)

    population = kfib(n, k)

    write_output_file(output_dir / io_file, str(population))


if __name__ == '__main__':
    main(f'rosalind_{Path(__file__).stem}.txt')
