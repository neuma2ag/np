from max3sat import parse, print_res
from random import choice


# Johnson's Algorithm
# https://cse.iitkgp.ac.in/~palash/2018AlgoDesignAnalysis/MAX3SAT_SLIDES.pdf
# Randomization Algorithm
# 2/3 Approximation for Max 3SAT, 7/8 for Max E3SAT
def approx(n_vars, clauses, silent=False):
    # O(n)
    assigments = [choice([True, False]) for _ in range(n_vars)]

    count = 0
    for c in clauses:
        if c.sat(assigments):
            count += 1

    if not silent:
        print_res(n_vars, count, assigments)


def main():
    (n_vars, clauses) = parse()
    approx(n_vars, clauses)


if __name__ == "__main__":
    main()
