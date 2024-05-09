from max3sat import Clause, exact, approx
from timeit import timeit
from functools import partial
from random import randint
import sys

sys.path.append("../code_solution")


def run_test(n_vars, sources):
    print("input:")
    print(sources)

    clauses = []
    for s in sources:
        clauses.append(Clause(s))

    print("exact:")
    exact(n_vars, clauses)
    print("approx:")
    approx(n_vars, clauses)


def random(n_vars, n_clauses, neg):
    included = set()
    sources = []

    for _ in range(n_clauses):
        source = []
        for _ in range(3):
            x = randint(1, n_vars)
            included.add(x)
            neg_chance = randint(0, 100)
            if neg_chance > neg:
                x *= -1
            source.append(x)
        sources.append(source)

    if len(included) != n_vars:
        random(n_vars, n_clauses, neg)
        return

    run_test(n_vars, sources)


def number(n):
    clauses = []
    xs = list(range(1, n + 1))
    for _ in range(n):
        clauses.append(Clause(xs))
    return (n, clauses)


def run_benchmark(func, text):
    print(text)
    (n_vars, clauses) = func()
    pe = partial(exact, n_vars, clauses, silent=True)
    et = timeit(pe, number=1)
    print("exact time:", et)
    pa = partial(approx, n_vars, clauses, silent=True)
    at = timeit(pa, number=1)
    print("approx time:", at)
    print()


if __name__ == "__main__":
    sources = [[1, -2, 3], [-1, 2, -3]]
    run_test(3, sources)
    print()

    random(2, 10, 50)
    random(5, 10, 50)
    random(10, 50, 50)

    ten = partial(number, 10)
    run_benchmark(ten, "TEN CLAUSES AND LITERALS")
    twenty = partial(number, 20)
    run_benchmark(twenty, "TWENTY CLAUSES AND LITERALS")
    twenty_four = partial(number, 24)
    run_benchmark(twenty_four, "TWENTY FOUR CLAUSES AND LITERALS")
    twenty_six = partial(number, 26)
    run_benchmark(twenty_six, "TWENTY SIX CLAUSES AND LITERALS")
