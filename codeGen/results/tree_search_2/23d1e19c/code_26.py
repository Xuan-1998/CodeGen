from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    parents = list(range(n+1))
    rank = [0] * (n+1)

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return
        if rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

    for u, v in edges:
        union(u-1, v-1)

    path = list(map(int, input().split()))
    res = [0, float('inf')]

    for i in range(1, len(path)):
        if find(path[i]-1) != find(path[i-1]-1):
            res[1] = min(res[1], 1)
            res[0] += 1
        else:
            res[0] += 1

    print(*res)

solve()
