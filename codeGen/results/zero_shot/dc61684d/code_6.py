from collections import defaultdict

# Step 1: Parse Input
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # Since the graph is non-directed

k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Step 5: Function to count connected components using DFS
def count_components(graph, n):
    visited = [False] * (n + 1)
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)
            components += 1
    return components

# Step 3: Initial Connectivity
initial_components = count_components(graph, n)

# Step 4: Experiments
for li, ri in experiments:
    # Temporarily remove the cable
    graph[li].remove(ri)
    graph[ri].remove(li)
    
    # Count the connected components with the cable removed
    print(count_components(graph, n))
    
    # Re-add the cable
    graph[li].append(ri)
    graph[ri].append(li)
