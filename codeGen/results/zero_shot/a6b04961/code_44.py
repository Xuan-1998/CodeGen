import sys

def find_max_beauty():
    n, m = map(int, input().split())
    graph = {i: set() for i in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    dp = [[0] * (n//2 + 1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i//2 + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (i-j))

    return max(max(row) for row in dp)

print(find_max_beauty())
