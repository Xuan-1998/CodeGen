class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            if self.rank[u_root] < self.rank[v_root]:
                self.parent[u_root] = v_root
            elif self.rank[u_root] > self.rank[v_root]:
                self.parent[v_root] = u_root
            else:
                self.parent[v_root] = u_root
                self.rank[u_root] += 1
            self.components -= 1

def main():
    n, m = map(int, input().split())
    ds = DisjointSet(n)
    edges = []

    for _ in range(m):
        x, y = map(int, input().split())
        edges.append((x - 1, y - 1))
        ds.union(x - 1, y - 1)

    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        # Temporarily remove the edge
        if ds.find(edges[l][0]) != ds.find(edges[l][1]):
            # The edge was the only connection between two components
            print(ds.components)
        else:
            # The edge is not the only connection, so no change in components
            print(ds.components - 1)
            # Note: We don't actually remove the edge from the data structure,
            # since it's only "temporarily" removed and we assume it's back
            # for the next experiment.

if __name__ == "__main__":
    main()
