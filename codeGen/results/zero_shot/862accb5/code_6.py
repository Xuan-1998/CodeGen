import sys
from collections import defaultdict
import heapq

def find_set(parent, i):
    if parent[i] == i:
        return i
    return find_set(parent, parent[i])

def union_set(parent, rank, x, y):
    xroot = find_set(parent, x)
    yroot = find_set(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(edges, n):
    parent = [i for i in range(n)]
    rank = [0] * n
    mst_edges = []
    mst_weight = 0
    for edge in edges:
        u, v, w = edge
        if find_set(parent, u) != find_set(parent, v):
            union_set(parent, rank, u, v)
            mst_edges.append(edge)
            mst_weight += w
    return mst_weight, mst_edges

def main():
    n = int(sys.stdin.readline().strip())
    edges = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        edges.append((u-1, v-1, l))
    edges.sort(key=lambda x: x[2])
    mst_weight, mst_edges = kruskal(edges, n)
    print(mst_weight)

if __name__ == "__main__":
    main()
