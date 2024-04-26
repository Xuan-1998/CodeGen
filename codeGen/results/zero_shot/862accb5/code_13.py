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
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def main():
    n = int(input().strip())
    roads = []
    for _ in range(n):
        u, v, l = map(int, input().strip().split())
        roads.append((l, u - 1, v - 1))  # Store roads with 0-based indexing

    # Sort roads by weight (length)
    roads.sort(reverse=True)

    dsu = DisjointSet(n)
    mst_weight = 0
    non_tree_edges = []

    # Kruskal's algorithm to find the spanning tree
    for l, u, v in roads:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_weight += l
        else:
            non_tree_edges.append(l)

    # The minimum inconvenience is the heaviest non-tree edge
    # because the graph will be connected with all lighter edges
    min_inconvenience = non_tree_edges[0] if non_tree_edges else 0

    print(min_inconvenience)

if __name__ == "__main__":
    main()
