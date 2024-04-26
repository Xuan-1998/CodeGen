import sys

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

def kruskal(edges, n):
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    edges.sort(key=lambda x: -x[2])  # Sort edges by weight in descending order
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
    return mst_edges, total_weight

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((u-1, v-1, l))  # Adjusting index to be 0-based
    mst_edges, total_weight = kruskal(edges, n)
    # The edge with the maximum weight is the last in the sorted list of mst_edges
    inconvenience = total_weight - mst_edges[-1][2]
    print(inconvenience)

if __name__ == "__main__":
    main()
