import sys

n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

visited = [False] * (n+1)
time_limit = 0
route = []

def dfs(vertex, time_left):
    global time_limit, route
    if visited[vertex]:
        return
    visited[vertex] = True
    for neighbor, edge_time in graph[vertex]:
        if edge_time <= time_left:
            if neighbor == n:
                route.append(vertex)
                time_limit += 1
            else:
                dfs(neighbor, time_left - edge_time)

dfs(1, T)
print(time_limit)
print(*route[::-1], sep='\n')
