import sys

def solve():
    n, = map(int, input().split())
    ws = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))

    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(max(ws[i-1], 1), 10**9 + 1):
            dp[i][j] = max(dp[i-1][min(j, ws[i-1]-edges[i-2][2])] + min(ws[i-1]-edges[i-2][2], j), 
                            dp[i-1][k] + k for k in range(min(j, ws[i-1]-edges[i-2][2])+1))

    print(dp[-1][-1])

solve()
