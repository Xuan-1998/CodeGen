import sys

def solve():
    n = int(input())
    dp = [float('inf')] * (n + 1)
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    parent = [-1] * (n + 1)

    for i in range(1, n):
        u, v = map(int, input().split())
        dp[v] = min(dp[v], dp[u] + 1)
        memo[u][v] = dp[v]

    capital = 0
    for i in range(1, n):
        if dp[i] < float('inf'):
            capital = i
            break

    print(dp[capital])

    path = []
    while parent[capital] != -1:
        path.append(capital)
        capital = parent[capital]
    path.reverse()
    print(*path)

solve()
