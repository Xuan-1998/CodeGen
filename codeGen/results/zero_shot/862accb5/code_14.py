import sys
from collections import defaultdict

# Disjoint Set Union (DSU) or Union-Find data structure to help with cycle detection
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                xroot, yroot = yroot, xroot
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

def kruskal(edges, n):
    dsu = DSU(n)
    mst_weight = 0
    max_edge = 0

    for weight, u, v in sorted(edges, reverse=True):
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_weight += weight
            max_edge = max(max_edge, weight)

    return mst_weight, max_edge

def main():
    n = int(sys.stdin.readline().strip())
    edges = []

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((l, u - 1, v - 1))  # Adjusting nodes to be zero-indexed

    total_weight, max_edge_weight = kruskal(edges, n)
    inconvenience = total_weight - max_edge_weight
    print(inconvenience)

if __name__ == "__main__":
    main()
