from random import randint


def exact(n_verts, adj_list):

    def dfs(u):
        max_dist = 0
        saved_path = []

        stack = [(u, 0, set([u]), [u])]

        while len(stack) > 0:
            u, dist, visited, path = stack.pop()
            for v in range(n_verts):
                weight = adj_list[u][v]
                if weight != float('-inf') and v not in visited:
                    new_dist = dist + weight
                    if new_dist > max_dist:
                        max_dist = new_dist
                        saved_path = path + [v]
                    stack.append((v, new_dist, visited | set([v]), path + [v]))

        return (max_dist, saved_path)

    maxi = (0, [])
    for u in range(n_verts):
        maxi = max(maxi, dfs(u))

    print(maxi)


def approx(n_verts, adj_list):

    def dfs(u):
        visited = [False] * n_verts
        dist = 0
        path = []
        stack = [u]

        while len(stack) > 0:
            u = stack.pop()
            path.append(u)

            maxi = (float('-inf'), None)
            for v in range(n_verts):
                weight = adj_list[u][v]
                if weight != float('-inf') and not visited[v]:
                    maxi = max(maxi, (weight, v))

            maxi, v = maxi
            if maxi != float('-inf'):
                dist += maxi
                stack.append(v)

        return (dist, path)

    tries = []
    if n_verts <= 10:
        tries = list(range(n_verts))
    else:
        for _ in range(10):
            x = randint(0, n_verts - 1)
            tries.append(x)
        tries = list(set(tries))

    maxi = (float('-inf'), None)
    for t in tries:
        maxi = max(maxi, dfs(t))

    return maxi


def parse():
    foo = input().split(' ')
    n_verts = int(foo[0])
    n_edges = int(foo[1])

    adj_list = [[float('-inf')] * n_verts for _ in range(n_verts)]
    verts = set()
    name_to_idx = {}
    idx_to_name = {}
    cur_idx = 0

    def add_vert(v):
        nonlocal cur_idx
        if v not in verts:
            verts.add(v)
            name_to_idx[v] = cur_idx
            idx_to_name[cur_idx] = v
            cur_idx += 1

    for _ in range(n_edges):
        foo = input().split(' ')
        u = str(foo[0])
        v = str(foo[1])
        weight = int(foo[2])
        add_vert(u)
        add_vert(v)
        adj_list[name_to_idx[u]][name_to_idx[v]] = weight

    return (n_verts, adj_list, idx_to_name)


if __name__ == "__main__":
    (n_verts, adj_list, idx_to_name) = parse()
    exact(n_verts, adj_list)
    print(approx(n_verts, adj_list))
