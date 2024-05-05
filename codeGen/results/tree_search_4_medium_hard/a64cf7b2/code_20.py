import sys

def dp(graph):
    n = len(graph)
    t_limit = int(sys.stdin.readline())
    visited = [[0] * (t_limit + 1) for _ in range(n + 1)]
    time = [0] * (n + 1)

    # Compute dynamic programming values
    for i in range(2, n + 1):
        for t in range(1, t_limit + 1):
            if visited[i - 1][t] and graph[i - 1][i - 1][0] <= t:
                visited[i][t] = max(visited[i][t], visited[i - 1][t - graph[i - 1][i - 1][2]] + 1)
                time[i] = min(time[i], time[i - 1] + graph[i - 1][i - 1][2])
            else:
                visited[i][t] = 0

    # Backtrack to construct the optimal route
    route = []
    t = t_limit
    for i in range(n, 0, -1):
        if visited[i][t]:
            route.append(i)
            t -= graph[route[-2]][i][2]
        else:
            break

    return len(route), ' '.join(map(str, reversed(route)))

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

# Read edges from stdin
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u].append((v, t))

k, route = dp(graph)
print(k)
print(route)
