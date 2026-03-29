from collections import deque

def dfs(graph, i):
    queue = deque([i])
    visited = [False] * (len(graph) + 1)
    visited[i] = True
    while queue:
        node = queue.popleft()
        for neighbor, time in graph[node]:
            if not visited[neighbor] and time <= T:
                queue.append(neighbor)
                visited[neighbor] = True
    return sum(visited)

def dp(graph, n, T):
    table = [[[0] * (T + 1)] * (n + 1)]
    
    for i in range(n - 1, -1, -1):
        for t in range(T, -1, -1):
            if t >= graph[i][0]:
                visited = 0
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    if table[n-1][t-graph[node][0]][node]:
                        visited += 1
                        for neighbor, time in graph[node]:
                            if time <= t - graph[neighbor][0] and not table[neighbor][t-time][neighbor]:
                                queue.append(neighbor)
                table[i][t] = visited + 1
            else:
                table[i][t] = 1

    return table[0][T]

def solve():
    n, m, T = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, t = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append((v, t))
    
    print(dp(graph, n, T))

solve()
