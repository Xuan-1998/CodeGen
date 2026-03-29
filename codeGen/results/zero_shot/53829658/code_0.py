import sys
from collections import defaultdict

# Read input
n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

# Function to find the centroid (average) of all cities
def calculate_centroid(cities):
    total_x = sum(x for x, _ in cities)
    total_y = sum(y for _, y in cities)
    return (total_x / len(cities), total_y / len(cities))

# Function to perform DFS and count the minimum number of edges needed to be reversed
def dfs(graph, start, visited, parent):
    min_reversals = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            if neighbor != parent:
                min_reversals += 1
            min_reversals += dfs(graph, neighbor, visited, start)
    return min_reversals

# Main program
capital_cities = list(range(1, n+1))
min_reversals = float('inf')

for capital in capital_cities:
    visited = set()
    parent = None
    for city in graph:
        if city != capital:
            visited.add(city)
            parent = capital
            min_reversals = min(min_reversals, dfs(graph, city, visited, parent))

print(min_reversals)

# Print all possible ways to choose the capital city (i.e., all permutations of the cities)
import itertools
for perm in itertools.permutations(capital_cities):
    print(' '.join(map(str, perm)))
