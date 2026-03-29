import sys

def read_input():
    n, m, T = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v, t))
    return n, m, T, edges

def solve(n, m, T, edges):
    # Initialize a table to store the maximum number of vertices that can be visited
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    # Build up the table using dynamic programming
    for u, v, t in edges:
        for i in range(T, t - 1, -1):
            if dp[u][i] > dp[v][i - t]:
                dp[v][i] = dp[u][i]
            else:
                dp[v][i] = max(dp[v][i], dp[u][i - t])
    
    # Find the maximum number of vertices that can be visited
    k = 0
    for i in range(n, 0, -1):
        if dp[i][T] > dp[i - 1][T]:
            k = i
            break
    
    return k

n, m, T, edges = read_input()
k = solve(n, m, T, edges)

print(k)
