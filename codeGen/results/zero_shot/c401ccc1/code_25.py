def infinite_zoo(q):
    parent = {}
    rank = {}

    def find(x):
        if x not in parent:
            parent[x] = x
            rank[x] = 0
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_u] = root_v
            if rank[root_u] == rank[root_v]:
                rank[root_v] += 1

    for _ in range(q):
        u, v = map(int, input().split())
        union(u, v)
        print("YES" if find(u) == find(v) else "NO")
