class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

    def count_components(self):
        # Count unique roots
        return len(set(self.find(i) for i in range(len(self.parent))))

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# For each experiment, count the number of connected components
for li, ri in experiments:
    uf = UnionFind(n)
    # Add all edges except the one being removed
    for i, (u, v) in enumerate(edges):
        if i + 1 != li:
            uf.union(u - 1, v - 1)  # Convert to 0-based index
    # Output the number of connected components
    print(uf.count_components())
