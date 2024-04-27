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

    def count_components(self):
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Initialize Union-Find structure
uf = UnionFind(n)

# Join sets for all edges except those to be removed in the experiments
for i, (x, y) in enumerate(edges, start=1):
    uf.union(x-1, y-1)

# Save the initial state of the Union-Find structure
initial_parent = uf.parent[:]
initial_rank = uf.rank[:]

# Perform experiments
for l, r in experiments:
    # Reset Union-Find structure to initial state
    uf.parent = initial_parent[:]
    uf.rank = initial_rank[:]

    # Join sets for all edges except the one to be removed
    for i, (x, y) in enumerate(edges, start=1):
        if i != l:
            uf.union(x-1, y-1)

    # Output the number of connected components
    print(uf.count_components())
