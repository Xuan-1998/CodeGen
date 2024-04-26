import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
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

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    longest_edge = 0
    
    for weight, u, v in sorted(edges):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            longest_edge = max(longest_edge, weight)
    
    return total_weight, longest_edge

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((l, u-1, v-1)) # Adjusting indices to be zero-based
    
    total_weight, longest_edge = kruskal(n, edges)
    
    # Subtract the longest edge from the total weight to get the minimum inconvenience
    print(total_weight - longest_edge)

if __name__ == "__main__":
    main()
