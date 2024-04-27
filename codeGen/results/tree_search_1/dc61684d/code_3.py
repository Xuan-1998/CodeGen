import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def count_components(uf, n):
    roots = set()
    for i in range(n):
        roots.add(uf.find(i))
    return len(roots)

def main():
    # Read the number of nodes (computers) and edges (cables)
    n, m = map(int, sys.stdin.readline().split())
    uf = UnionFind(n)
    edges = []

    # Read the edges and construct the graph
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        edges.append((x - 1, y - 1))
        uf.union(x - 1, y - 1)

    # Read the number of experiments
    k = int(sys.stdin.readline())

    # Perform the experiments
    for _ in range(k):
        li, ri = map(int, sys.stdin.readline().split())
        li -= 1
        ri -= 1

        # Create a new UnionFind structure for the experiment
        temp_uf = UnionFind(n)
        for i, (x, y) in enumerate(edges):
            if i != li and i != ri:
                temp_uf.union(x, y)

        # Count and print the number of connected components
        print(count_components(temp_uf, n))

if __name__ == "__main__":
    main()
