import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_edges = []
    max_edge_weight = 0
    for weight, u, v in sorted(edges):
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            max_edge_weight = max(max_edge_weight, weight)
    return mst_edges, max_edge_weight

def main():
    n = int(input().strip())
    edges = []
    for _ in range(n):
        u, v, l = map(int, input().split())
        edges.append((l, u - 1, v - 1))

    mst_edges, max_edge_weight = kruskal(n, edges)
    total_inconvenience = sum(weight for _, _, weight in mst_edges) - max_edge_weight
    print(total_inconvenience)

if __name__ == "__main__":
    main()
