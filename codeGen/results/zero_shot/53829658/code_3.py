# Step 3: Calculate the minimum number of roads to be inversed
def find_centroid(graph):
    n = len(graph) - 1
    children = [0] * (n+1)
    for i in range(1, n+1):
        if graph[i]:
            children[len(graph[i])] += 1
    centroid = max(range(n), key=lambda x:children[x])
    return centroid

def dfs(graph, parent, depth):
    global min_distance
    global centroid
    children = [0] * (n+1)
    for i in range(1, n+1):
        if graph[i] and i != parent:
            children[len(graph[i])] += 1
    max_children = max(range(n), key=lambda x:children[x])
    if depth > centroid or not children[max_children]:
        min_distance = min(min_distance, depth)
    for i in range(1, n+1):
        if graph[i] and i != parent:
            dfs(graph, i, depth + 1)

min_distance = float('inf')
centroid = find_centroid(graph)
dfs(graph, -1, 0)

# Step 4: Find all possible ways to choose the capital
def traverse(graph, node, path):
    if len(path) == n:
        print(' '.join(map(str, path)))
        return
    for neighbor in graph[node]:
        if neighbor not in path:
            traverse(graph, neighbor, path + [neighbor])

# Step 5: Print the minimum number of roads to be inversed and all possible ways to choose the capital
print(min_distance)
traverse(graph, find_centroid(graph), [])
