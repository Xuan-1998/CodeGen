import sys

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(edges, n):
    uf = UnionFind(n)
    mst_weight = 0
    max_edge_in_mst = (0, 0, 0)
    
    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight
            if weight > max_edge_in_mst[2]:
                max_edge_in_mst = edge

    return mst_weight, max_edge_in_mst

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((u - 1, v - 1, l))  # Convert to 0-based indexing

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Find MST and the maximum weighted edge in the MST
    mst_weight, max_edge_in_mst = kruskal(edges, n)

    # The minimum inconvenience is the total weight of the MST
    # minus the weight of the maximum edge in the MST
    min_inconvenience = mst_weight - max_edge_in_mst[2]
    print(min_inconvenience)

if __name__ == "__main__":
    main()
