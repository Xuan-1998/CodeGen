# Step 1: Read the input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))  # subtract 1 because array indices are 0-based

# Step 2: Initialize the graph as an adjacency list
graph = [[] for _ in range(n)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# Step 3: Find all connected components (hedgehog tails)
tails = []
visited = [False] * n
def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

for i in range(n):
    if not visited[i]:
        tails.append([])
        dfs(i)
        for j in range(1, len(tails[-1])):
            tails[-1][j-1], tails[-1][j] = tails[-1][j], tails[-1][j-1]

# Step 4: Count the number of spines (edges not in any tail)
spines = sum(len(graph[i]) for i in range(n)) - len(edges)

# Step 5: Calculate the maximum possible beauty
beauty = max(len(tail) * (n - len(tail)) for tail in tails) * spines

print(beauty)
