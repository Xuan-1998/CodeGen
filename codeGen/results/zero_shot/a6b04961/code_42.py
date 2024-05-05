import sys
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    parent = {}
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    parent[neighbor] = node
    return visited, parent

def find_longest_path(graph):
    longest_path = 0
    tail = []
    current_node = None
    for node in sorted(list(graph)):
        if current_node is None or graph[current_node].index(node) < len(graph[current_node]):
            current_node = node
            tail.append(current_node)
        else:
            if len(tail) > longest_path:
                longest_path = len(tail)
            tail = [current_node]
            current_node = node
    if len(tail) > longest_path:
        longest_path = len(tail)
    return longest_path, tail

def find_spines(graph, tail):
    spines = 0
    for edge in graph:
        if edge[0] not in tail and edge[1] not in tail:
            spines += 1
    return spines

n, m = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

longest_path, tail = find_longest_path(graph)
spines = find_spines(graph, tail)
print(longest_path * spines)
