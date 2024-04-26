class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def count_trees(p):
    uf = UnionFind(max(p) + 1)
    for i, x in enumerate(p):
        uf.union(x - 1, p[x] - 1)
    return len(set(uf.find(i) for i in range(len(p))))

n = int(input())
p = [int(x) for x in input().split()]
print(count_trees(p))
