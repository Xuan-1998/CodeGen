import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def kruskal(edges, n):
    uf = UnionFind(n)
    mst_weight = 0
    max_edge_in_mst = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            max_edge_in_mst = max(max_edge_in_mst, weight)

    return mst_weight - max_edge_in_mst

def main():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((l, u - 1, v - 1))  # Convert to 0-based index

    edges.sort()  # Sort edges by weight
    min_inconvenience = kruskal(edges, n)
    print(min_inconvenience)

if __name__ == "__main__":
    main()
