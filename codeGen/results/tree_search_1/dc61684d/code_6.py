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

    def count_components(self):
        return sum(self.parent[i] == i for i in range(len(self.parent)))

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Initialize Union-Find structure
uf = UnionFind(n)

# Join all nodes that are directly connected by an edge
for x, y in edges:
    uf.union(x - 1, y - 1)

# Perform experiments
for l, r in experiments:
    # Make a copy of Union-Find structure
    uf_copy = UnionFind(n)
    uf_copy.parent = uf.parent[:]
    uf_copy.rank = uf.rank[:]

    # Disconnect the specified edge by skipping the union operation for this edge
    for i, (x, y) in enumerate(edges):
        if i + 1 != l:
            uf_copy.union(x - 1, y - 1)

    # Count and output the number of connected components
    print(uf_copy.count_components())
