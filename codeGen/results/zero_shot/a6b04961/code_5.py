import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def dfs(graph, visited, vertex, path):
    # TO DO: implement DFS algorithm
    pass

n, m, edges = read_input()

# TO DO: construct the hedgehog using DFS or BFS
