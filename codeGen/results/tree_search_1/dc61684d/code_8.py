class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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

def count_components(uf, n):
    return sum(1 for i in range(n) if uf.find(i) == i)

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(k)]

    # Initialize Union-Find
    uf = UnionFind(n)

    # Union sets based on the provided edges
    for x, y in edges:
        uf.union(x - 1, y - 1)  # Adjusting for 0-based indexing

    # Perform experiments
    for l, r in experiments:
        # Disconnect the edge
        original_parent = uf.parent[:]
        original_rank = uf.rank[:]

        uf.union(edges[l - 1][0] - 1, edges[l - 1][1] - 1)

        # Count connected components
        print(count_components(uf, n))

        # Reconnect the edge
        uf.parent = original_parent
        uf.rank = original_rank

if __name__ == "__main__":
    main()
