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
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

    def count_components(self):
        return len(set(self.find(x) for x in range(len(self.parent))))

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Initialize DSU
dsu = DSU(n)

# Union all the edges
for x, y in edges:
    dsu.union(x - 1, y - 1)

# Perform experiments
for li, ri in experiments:
    # Make a copy of the DSU
    dsu_copy = DSU(n)
    dsu_copy.parent = dsu.parent[:]
    dsu_copy.rank = dsu.rank[:]

    # Temporarily remove the edge
    dsu_copy.union(edges[li - 1][0] - 1, edges[ri - 1][1] - 1)

    # Count the number of connected components
    print(dsu_copy.count_components())
