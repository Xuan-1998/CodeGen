# Read the input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))

# Initialize variables
visited = [False]*n
tail = [-1]
spines = 0

# DFS to find the longest tail possible
def dfs(node):
    global tail, spines
    visited[node] = True
    for edge in edges:
        if edge[0] == node and not visited[edge[1]]:
            dfs(edge[1])
        elif edge[1] == node and not visited[edge[0]]:
            dfs(edge[0])
    tail.append(node)
    nonlocal spines
    for edge in edges:
        if edge[0] == node and edge[1] not in tail:
            spines += 1

# Perform DFS to find the longest possible tail
for i in range(n):
    if not visited[i]:
        dfs(i)

# Calculate the beauty of the hedgehog
beauty = len(tail) * (m - len(edges))
print(beauty)
