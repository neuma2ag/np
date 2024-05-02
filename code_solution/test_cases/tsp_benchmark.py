import math
import random
from code_solution.tsp import exact, approximate
import sys

sys.path.insert(0, "../")


def simple():
    n_verts = 3
    adj_list = [[float('inf')] * n_verts for _ in range(n_verts)]
    adj_list[0][1] = 3
    adj_list[1][0] = 3
    adj_list[1][2] = 4
    adj_list[2][1] = 4
    adj_list[0][2] = 5
    adj_list[2][0] = 5

    run_test(n_verts, adj_list)


def generator(n, m):
    def dist(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    points = [[random.randint(0, m), random.randint(0, m)] for i in range(n)]
    adj_list = [[dist(points[i], points[j]) for i in range(n)]
                for j in range(n)]
    return (n, adj_list)


def run_test(n_verts, adj_list):
    print("input:")
    for row in adj_list:
        print(row)

    print("exact:")
    dist, path = exact(n_verts, adj_list)
    print(dist)
    print(*path)

    print("approx:")
    dist, path = approximate(n_verts, adj_list)
    print(dist)
    print(*path)


def rand(n, m):
    n_verts, adj_list = generator(n, m)
    run_test(n_verts, adj_list)


if __name__ == "__main__":
    simple()
    rand(5, 10)
    rand(10, 20)
