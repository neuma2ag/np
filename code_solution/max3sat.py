class Clause:
    def __init__(self, source):
        self.source = source

    def sat(self, vars):
        for literal in self.source:
            idx = abs(literal) - 1
            if literal > 0 and vars[idx] or literal < 0 and not vars[idx]:
                return True

        return False


def parse():
    foo = input().split(' ')
    n_vars = int(foo[0])
    n_clauses = int(foo[1])

    clauses = []
    for _ in range(n_clauses):
        source = [int(x) for x in input().split(' ')]
        clauses.append(Clause(source))

    return (n_vars, clauses)


def print_res(n_vars, maxi, perm):
    print(maxi)
    for i in range(n_vars):
        print(i + 1, end=' ')
        print('T') if perm[i] else print('F')
