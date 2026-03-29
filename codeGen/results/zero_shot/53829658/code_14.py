# Step 1: Read the input
n = int(input())
roads = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

# Step 2: Create a graph representation using an adjacency list
graph = [[] for _ in range(n+1)]
for road in roads:
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0]) # Assuming the graph is undirected

# Step 3: Find the root of each connected component using DFS
roots = []
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        roots.append(i)
        dfs(graph, i, visited)

# Step 4: Calculate the centroid of each connected component
centroids = []
for root in roots:
    visited = [False] * (n+1)
    parent = {}
    dfs(graph, root, visited, parent)
    centroid = find_centroid(parent, visited)
    centroids.append(centroid)

# Step 5: Choose the capital city that minimizes the number of edges to be reversed
capital = min(centroids, key=lambda x: len(x))

# Step 6: Find all possible ways to choose the capital
capitals = []
for root in roots:
    visited = [False] * (n+1)
    parent = {}
    dfs(graph, root, visited, parent)
    capital_path = find_capital_path(parent, visited)
    capitals.append(capital_path)

# Step 7: Print the results
print(len(capitals[0]))  # Minimum number of edges to be reversed
for path in capitals:
    print(' '.join(map(str, path)))
