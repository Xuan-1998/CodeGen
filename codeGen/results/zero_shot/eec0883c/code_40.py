# Step 1: Read input
n = int(input())
w = list(map(int, input().split()))
edges = []
for i in range(n-1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

# Step 2: Build the graph
graph = {}
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]] = []
    if edge[1] not in graph:
        graph[edge[1]] = []
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))

# Step 3: Find the maximum amount of gasoline
def dfs(node, remaining_gasoline):
    if node not in visited:
        visited.add(node)
        max_gasoline = min(remaining_gasoline, w[node-1])
        for neighbor, length in graph[node]:
            if neighbor not in visited:
                max_gasoline = max(max_gasoline, dfs(neighbor, remaining_gasoline-length))
        return max_gasoline
    else:
        return 0

# Step 4: Print the answer
visited = set()
max_gasoline = dfs(1, w[0])
print(max_gasoline)
