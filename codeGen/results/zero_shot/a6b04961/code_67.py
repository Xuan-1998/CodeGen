import sys
from collections import defaultdict, deque

# Read input
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Step 1: Find all connected components in the graph
visited = set()
connected_components = []
for i in range(n):
    if i not in visited:
        component = deque([i])
        while component:
            vertex = component.popleft()
            if vertex not in visited:
                visited.add(vertex)
                component.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

        connected_components.append(list(component))

# Step 2: Find the maximum possible beauty of a hedgehog
max_beaauty = 0
for _ in range(len(connected_components)):
    # Step 2.1: Find the longest tail
    max_tail_length = 0
    for component in connected_components:
        tail_length = 0
        for vertex in component:
            if all(neighbor not in component for neighbor in graph[vertex]):
                tail_length += 1
            else:
                break
        max_tail_length = max(max_tail_length, tail_length)

    # Step 2.2: Find the maximum number of spines
    max_spines = 0
    for i in range(len(connected_components)):
        for j in range(i + 1, len(connected_components)):
            for vertex in connected_components[i]:
                if any(neighbor not in connected_components[j] for neighbor in graph[vertex]):
                    max_spines += 1

    # Step 2.3: Calculate the maximum beauty
    max_beaauty = max(max_beaauty, max_tail_length * (max_spines + 1))

print(max_beauty)
