from itertools import product


class Clause:
    def __init__(self, source):
        self.source = source

    def sat(self, vars):
        for literal in self.source:
            idx = abs(literal) - 1
            if literal > 0 and vars[idx] or literal < 0 and not vars[idx]:
                return True

        return False


def exact(n_vars, clauses, silent=False):
    # O(2^n here)
    perms = [list(x) for x in product([True, False], repeat=n_vars)]

    maxi = 0
    perm = None
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


def approx(n_vars, clauses, silent=False):
    t = [True] * n_vars
    f = [False] * n_vars

    fn = 0
    for c in clauses:
        if c.sat(f):
            fn += 1

    tn = 0
    for c in clauses:
        if c.sat(t):
            tn += 1

    if not silent:
        print_res(n_vars, fn, f) if fn > tn else print_res(n_vars, tn, t)


def print_res(n_vars, maxi, perm):
    print(maxi)
    for i in range(n_vars):
        print(i + 1, end=' ')
        print('T') if perm[i] else print('F')


def parse():
    foo = input().split(' ')
    n_vars = int(foo[0])
    n_clauses = int(foo[1])

    clauses = []
    for _ in range(n_clauses):
        source = [int(x) for x in input().split(' ')]
        clauses.append(Clause(source))

    return (n_vars, clauses)


if __name__ == "__main__":
    (n_vars, clauses) = parse()

    print("\nexact:")
    exact(n_vars, clauses)

    print("\napprox:")
    approx(n_vars, clauses)
