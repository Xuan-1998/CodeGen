import sys

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        self.parent[yr] = xr
        return True

def kruskal(edges, n):
    dsu = DisjointSetUnion(n)
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in sorted(edges, reverse=True):
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v))
    
    return mst_weight, mst_edges

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    total_weight = 0
    
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((l, u-1, v-1))  # Subtracting 1 to use 0-based indexing
        total_weight += l

    mst_weight, mst_edges = kruskal(edges, n)
    min_inconvenience = total_weight - mst_weight
    
    print(min_inconvenience)

if __name__ == "__main__":
    main()
