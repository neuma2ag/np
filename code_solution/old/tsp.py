from queue import PriorityQueue


def exact(n_verts, adj_list):
    visited = set([0])
    order = [0]
    saved = [0]

    def inner(u: int):
        nonlocal saved

        if len(visited) == n_verts:
            return adj_list[0][u]

        dist = float('inf')
        for v in range(n_verts):
            if v not in visited:
                visited.add(v)
                order.append(v)
                new_dist = adj_list[u][v] + inner(v)
                if new_dist < dist:
                    dist = new_dist
                    saved = order.copy()

                order.pop()
                visited.remove(v)

        return dist

    dist = inner(0)
    saved.append(0)
    return (dist, saved)


def approximate(n_verts, adj_list):
    visited = set()
    visited.add(0)

    mst_adj_list = [[0] * n_verts for _ in range(n_verts)]

    q = PriorityQueue()
    for v in range(1, n_verts):
        weight = adj_list[0][v]
        if weight != float('inf'):
            q.put((weight, 0, v))

    while len(visited) < n_verts:
        (weight, u, v) = q.get()
        if v not in visited:
            visited.add(v)
            mst_adj_list[u][v] = weight
            mst_adj_list[v][u] = weight

            for w in range(0, n_verts):
                weight = adj_list[v][w]
                if weight != float('inf'):
                    q.put((weight, v, w))

    visited = set([0])
    order = [0]

    def traverse(u):
        mini = (float('inf'), None)
        for v in range(n_verts):
            weight = adj_list[u][v]
            if weight != float('inf') and v not in visited:
                mini = min(mini, (weight, v))

        _, v = mini
        if v:
            visited.add(v)
            order.append(v)
            traverse(v)

    traverse(u)
    order.append(0)

    dist = 0
    for i in range(len(order) - 1):
        u = order[i]
        v = order[i + 1]
        dist += adj_list[u][v]

    return (dist, order)


def parse():
    foo = input().split(' ')
    n_verts = int(foo[0])
    n_edges = int(foo[1])

    adj_list = [[float('inf')] * n_verts for _ in range(n_verts)]
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
        u_idx = name_to_idx[u]
        v_idx = name_to_idx[v]
        adj_list[u_idx][v_idx] = weight
        adj_list[v_idx][u_idx] = weight

    return (n_verts, adj_list, idx_to_name)


def print_res(res, idx_to_name):
    (dist, path) = res
    for i in range(len(path)):
        path[i] = idx_to_name[path[i]]

    print(dist)
    print(*path)


if __name__ == "__main__":
    (n_verts, adj_list, idx_to_name) = parse()

    print("\nexact:")
    res = exact(n_verts, adj_list)
    print_res(res, idx_to_name)

    print("\napproximate:")
    res = approximate(n_verts, adj_list)
    print_res(res, idx_to_name)
