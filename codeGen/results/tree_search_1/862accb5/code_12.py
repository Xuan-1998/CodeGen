import sys

class DisjointSet:
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
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def kruskal(n, edges):
    dsu = DisjointSet(n)
    mst_weight = 0
    for u, v, weight in sorted(edges, key=lambda x: x[2]):
        if dsu.union(u, v):
            mst_weight += weight
    return mst_weight

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    total_weight = 0
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1, l))  # Adjusting for 0-based indexing
        total_weight += l

    mst_weight = kruskal(n, edges)
    inconvenience = total_weight - mst_weight
    print(inconvenience)

if __name__ == "__main__":
    main()
