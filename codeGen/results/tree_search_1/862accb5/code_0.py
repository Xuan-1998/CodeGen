import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1
            return True
        return False

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    max_edge_in_mst = 0

    for u, v, weight in sorted(edges, key=lambda x: x[2]):
        if uf.union(u, v):
            mst_weight += weight
            max_edge_in_mst = max(max_edge_in_mst, weight)

    return mst_weight - max_edge_in_mst

def main():
    n = int(sys.stdin.readline())
    edges = []

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1, l))  # Adjusting for zero-based indexing

    result = kruskal(n, edges)
    print(result)

if __name__ == "__main__":
    main()
