from itertools import product
from max3sat import parse, print_res


def exact(n_vars, clauses, silent=False):
    # O(2^n) here
    perms = [list(x) for x in product([True, False], repeat=n_vars)]

    maxi = 0
    perm = None
    # O(2^n * c)
    for p in perms:

        count = 0
        for c in clauses:
            if c.sat(p):
                count += 1

        if count > maxi:
            maxi = count
            perm = p

    if not silent:
        print_res(n_vars, maxi, perm)


def main():
    (n_vars, clauses) = parse()
    exact(n_vars, clauses)


if __name__ == "__main__":
    main()
