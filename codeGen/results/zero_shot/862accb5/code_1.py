import sys

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

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_edges = []
    edges.sort(key=lambda x: x[2])  # Sort edges by length
    for u, v, l in edges:
        if uf.union(u - 1, v - 1):
            mst_edges.append((u, v, l))
    return mst_edges

def main():
    n = int(sys.stdin.readline().strip())
    edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    mst_edges = kruskal(n, edges)
    max_edge_length = max(l for u, v, l in mst_edges)
    min_inconvenience = sum(l for u, v, l in mst_edges) - max_edge_length
    print(min_inconvenience)

if __name__ == "__main__":
    main()
