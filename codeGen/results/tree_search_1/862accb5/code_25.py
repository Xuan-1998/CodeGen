import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    max_edge = 0
    for weight, u, v in sorted(edges, reverse=True):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight
            max_edge = max(max_edge, weight)
    return mst_weight, max_edge

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((l, u - 1, v - 1))
    
    mst_weight, max_edge = kruskal(n, edges)
    print(mst_weight - max_edge)

if __name__ == "__main__":
    main()
