import sys

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

def dfs(node, parent, visited, tail):
    # Count the number of spines
    spine_count = 0
    for neighbor in edges:
        if neighbor[0] == node and neighbor[1] not in visited:
            spine_count += 1
        elif neighbor[1] == node and neighbor[0] not in visited:
            spine_count += 1

    # Update the maximum beauty
    global max_beauty
    max_beauty = max(max_beauty, len(tail) * (spine_count + 1))

    # Recursively explore the graph
    for neighbor in edges:
        if neighbor[0] == node and neighbor[1] not in visited:
            dfs(neighbor[1], node, visited | {neighbor[1]}, tail + [neighbor[1]])
        elif neighbor[1] == node and neighbor[0] not in visited:
            dfs(neighbor[0], node, visited | {neighbor[0]}, tail + [neighbor[0]])

# Initialize the variables
max_beauty = 0
visited = set()
tail = []

# Start DFS from an arbitrary node (e.g., node 1)
dfs(1, -1, set(), [])

print(max_beauty)
