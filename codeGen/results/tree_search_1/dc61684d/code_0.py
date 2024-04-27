import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.component_count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
            self.component_count -= 1

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        edges.append((x-1, y-1))  # Subtract 1 for zero-based indexing

    dsu = DSU(n)
    for x, y in edges:
        dsu.union(x, y)

    k = int(sys.stdin.readline())
    for _ in range(k):
        li, ri = map(int, sys.stdin.readline().split())
        li, ri = li-1, ri-1  # Subtract 1 for zero-based indexing

        # Temporarily disconnect the cable
        original_count = dsu.component_count
        x_root = dsu.find(edges[li][0])
        y_root = dsu.find(edges[li][1])
        if x_root != y_root:
            dsu.component_count += 1

        print(dsu.component_count)

        # Restore the original component count
        dsu.component_count = original_count

if __name__ == "__main__":
    main()
