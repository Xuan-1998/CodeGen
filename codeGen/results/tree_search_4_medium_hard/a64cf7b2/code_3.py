import sys

def solve():
    n, m, T = map(int, input().split())
    dp = [[-float('inf')] * (T + 1) for _ in range(n + 1)]

    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u - 1, v - 1, t))

    for i in range(1, n + 1):
        dp[i][0] = 1

    for u, v, w in edges:
        for j in range(T, w - 1, -1):
            if dp[u][j] != -float('inf'):
                dp[v][j - w] = max(dp[v][j - w], dp[u][j] + 1)

    max_visited = 0
    for t in range(1, T + 1):
        if dp[n][T - t] != -float('inf'):
            max_visited = dp[n][T - t]
            break

    print(max_visited)
    visited_vertices = []
    time_left = T
    current_vertex = n
    while time_left > 0:
        for vertex, edge_weight in edges:
            if vertex == current_vertex and time_left >= edge_weight:
                visited_vertices.append(vertex + 1)
                time_left -= edge_weight
                current_vertex = vertex
                break

    print(*visited_vertices, sep='\n')

if __name__ == '__main__':
    solve()
