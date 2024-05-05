import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1

    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
        union(u, v)

    dp = defaultdict(bool)
    dp[(0, k-1)] = True
    for edge in edges:
        u, v = edge
        x = find(u)
        y = find(v)
        if x != y:
            new_k = max(0, k - 1)
            dp[(x, new_k)] |= dp[(y, k-1-new_k)]
    print('YES' if dp[(0, k-1)] else 'NO')

if __name__ == "__main__":
    solve()
