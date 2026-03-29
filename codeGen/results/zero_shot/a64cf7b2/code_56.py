n = int(input())
m = int(input())
T = int(input())

edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

graph = [[] for _ in range(n + 1)]
for u, v, t in edges:
    graph[u].append((v, t))
    graph[v].append((u, T - t))

def dfs(v, time_left):
    if time_left < 0:
        return False
    if graph[v]:
        for neighbor, edge_time in graph[v]:
            if dfs(neighbor, time_left - edge_time):
                return True
    return True

max_visited = 0
path = []
for i in range(n + 1):
    if dfs(i, T):
        max_visited += 1
        path.append(i)

print(max_visited)
print(*path, sep=' ')
