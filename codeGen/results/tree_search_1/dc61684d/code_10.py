class DisjointSet:
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
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    def count_sets(self):
        return sum(1 for i in range(len(self.parent)) if self.find(i) == i)

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(k)]
    
    ds = DisjointSet(n)
    for x, y in edges:
        ds.union(x - 1, y - 1)
    
    initial_components = ds.count_sets()
    
    for l, r in experiments:
        # Temporarily remove the edge by making a new disjoint set
        temp_ds = DisjointSet(n)
        for i, (x, y) in enumerate(edges):
            if i + 1 != l:  # Skip the edge to be removed
                temp_ds.union(x - 1, y - 1)
        print(temp_ds.count_sets() - initial_components + 1)

if __name__ == "__main__":
    main()
