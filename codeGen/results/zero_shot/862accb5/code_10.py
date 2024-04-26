import sys

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
                self.rank[rootU] += 1

    def set_size(self, u):
        return self.size[self.find(u)]

def main():
    n = int(sys.stdin.readline().strip())
    roads = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    uf = UnionFind(n + 1)
    total_inconvenience = 0
    
    for u, v, l in roads:
        uf.union(u, v)
        total_inconvenience += l
    
    min_inconvenience = total_inconvenience
    for u, v, l in roads:
        if uf.find(u) != uf.find(v):
            # This is a critical edge, removing it will disconnect the graph
            continue
        inconvenience_without_edge = total_inconvenience - l
        min_inconvenience = min(min_inconvenience, inconvenience_without_edge)
    
    print(min_inconvenience)

if __name__ == "__main__":
    main()
