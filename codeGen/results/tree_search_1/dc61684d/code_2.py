class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

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
            self.components -= 1

    def get_component_count(self):
        return self.components

# Read number of computers and cables
n, m = map(int, input().split())

# Initialize Union-Find
uf = UnionFind(n)

# Read and add cables to the Union-Find
edges = []
for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x - 1, y - 1))  # Adjusting for zero-based indexing
    uf.union(x - 1, y - 1)

# Read number of experiments
k = int(input())

# Perform experiments
for _ in range(k):
    uf_copy = UnionFind(n)
    uf_copy.parent = uf.parent.copy()
    uf_copy.rank = uf.rank.copy()
    uf_copy.components = uf.components

    # Read the cable to disconnect and adjust for zero-based indexing
    li, ri = map(int, input().split())
    li -= 1
    ri -= 1

    # Reconnect all cables except the one to be disconnected
    for i, (x, y) in enumerate(edges):
        if i != li and i != ri:
            uf_copy.union(x, y)

    # Output the number of connected components after the disconnection
    print(uf_copy.get_component_count())
