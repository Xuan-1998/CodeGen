import sys

def dfs(node, parent, remaining_gasoline):
    # Update the maximum gasoline that Nut can have at the end of the path
    global max_gasoline

    if node == target_node:
        max_gasoline = max(max_gasoline, remaining_gasoline)
    else:
        for neighbor in graph[node]:
            if neighbor != parent:
                new_remaining_gasoline = min(remaining_gasoline - 1, w[neighbor])
                dfs(neighbor, node, new_remaining_gasoline)

# Main function
n = int(sys.stdin.readline())
w = [int(x) for x in sys.stdin.readline().split()]
graph = {}
for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# Find the target node (the city we want to reach)
target_node = int(sys.stdin.readline())

max_gasoline = 0

# Start DFS from the starting node
dfs(1, None, w[1])

print(max_gasoline)
