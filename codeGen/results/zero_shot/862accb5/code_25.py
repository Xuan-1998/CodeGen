import sys

class UnionFind:
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
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

def main():
    n = int(sys.stdin.readline())
    edges = []

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((l, u - 1, v - 1))

    # Sort the edges by weight in non-decreasing order
    edges.sort()

    # Initialize UnionFind to manage connected components
    uf = UnionFind(n)

    # Initialize the maximum edge weight to 0
    max_edge_weight = 0

    # Iterate over the sorted edges to construct the spanning tree
    for l, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            max_edge_weight = max(max_edge_weight, l)

    # Output the minimum possible inconvenience
    sys.stdout.write(str(max_edge_weight))

if __name__ == "__main__":
    main()
