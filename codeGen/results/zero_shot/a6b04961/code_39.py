import sys
from collections import deque, defaultdict

# Input graph edges
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Function to find the maximum beauty of a hedgehog
def max_beauty():
    # Initialize visited set and distance array for BFS
    visited = set()
    distance = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)

    # Perform BFS from each unvisited node to find the longest path
    for i in range(1, n + 1):
        if i not in visited:
            queue = deque([(i, 0)])  # (node, distance)
            while queue:
                node, dist = queue.popleft()
                if dist > distance[node]:
                    continue
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = node
                        queue.append((neighbor, dist + 1))
                        distance[neighbor] = dist + 1

    # Initialize variables to keep track of the longest tail and spine count
    max_tail_length = 0
    spines = 0

    # Traverse the graph in topological order using the BFS traversal results
    visited = set()
    for i in range(1, n + 1):
        if i not in visited:
            node = i
            tail_length = 0
            while parent[node] != -1:
                tail_length += 1
                node = parent[node]
            max_tail_length = max(max_tail_length, tail_length)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    spines += 1

    # Calculate and print the maximum possible beauty of a hedgehog
    return max_tail_length * spines

# Print the solution
print(max_beauty())
