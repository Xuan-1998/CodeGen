import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, graph

def find_longest_path(graph):
    visited = set()
    longest_path = 0
    for node in graph:
        if node not in visited:
            path_length = dfs(node, visited, 1, graph)
            longest_path = max(longest_path, path_length)
    return longest_path

def dfs(node, visited, length, graph):
    if node in visited:
        return 0
    visited.add(node)
    path_length = length
    for neighbor in graph[node]:
        path_length = max(path_length, dfs(neighbor, visited, length + 1, graph))
    visited.remove(node)
    return path_length

def solve(n, graph):
    longest_path = find_longest_path(graph)
    spines = sum(len(neighbors) - 1 for neighbors in graph.values())
    return longest_path * spines

if __name__ == "__main__":
    n, graph = read_input()
    print(solve(n, graph))
