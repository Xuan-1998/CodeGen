import sys
import itertools

n = int(sys.stdin.readline())

graph = {}
for _ in range(n-1):
    si, ti = map(int, sys.stdin.readline().split())
    if si not in graph:
        graph[si] = []
    if ti not in graph:
        graph[ti] = []
    graph[si].append(ti)

def find_center(graph):
    max_distance = 0
    center = None
    for city in graph:
        distance = dfs(graph, city)
        if distance > max_distance:
            max_distance = distance
            center = city
    return center

def dfs(graph, city, visited=None):
    if visited is None:
        visited = set()
    visited.add(city)
    max_depth = 0
    for neighbor in graph[city]:
        if neighbor not in visited:
            depth = dfs(graph, neighbor, visited)
            if depth > max_depth:
                max_depth = depth
    return max_depth + 1

center = find_center(graph)

def count_reversals(graph, center):
    reversals = 0
    for city in graph:
        if city != center and (city not in graph[center] or len(graph[center]) > 1):
            reversals += 1
    return reversals

reversals = count_reversals(graph, center)

print(reversals)
print(len(find_capitals(graph)))
for capital in find_capitals(graph):
    print(*capital)
