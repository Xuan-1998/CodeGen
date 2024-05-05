import sys

# Read input
n = int(sys.stdin.readline())
edges = []
for _ in range(n - 1):
    si, ti = map(int, sys.stdin.readline().split())
    edges.append((si, ti))

# Sort edges by orientation (topological order)
edges.sort(key=lambda x: x[0])

# Initialize capital cities set
capital_cities = set()

# Find the optimal capital city using a greedy approach
optimal_capital = None
for edge in edges:
    si, ti = edge
    if ti not in capital_cities:
        capital_cities.add(si)
    else:
        optimal_capital = si
        break

# Calculate the minimum number of reversed roads
reversed_roads = 0
for edge in edges:
    si, ti = edge
    if si == optimal_capital:
        reversed_roads += 1

# Print output
print(reversed_roads)
print(*capital_cities, sep='\n')
