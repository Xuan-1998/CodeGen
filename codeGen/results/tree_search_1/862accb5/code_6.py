import sys

class DisjointSet:
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
    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = []
    for w, u, v in sorted(edges):
        if ds.union(u, v):
            mst_weight += w
            mst_edges.append((u, v))
    return mst_weight, mst_edges

def main():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((l, u - 1, v - 1))  # Subtracting 1 to use 0-indexed vertices

    mst_weight, mst_edges = kruskal(n, edges)
    max_non_mst_edge_weight = max(w for w, u, v in edges if (u, v) not in mst_edges and (v, u) not in mst_edges)
    min_inconvenience = mst_weight - max_non_mst_edge_weight
    print(min_inconvenience)

if __name__ == "__main__":
    main()
