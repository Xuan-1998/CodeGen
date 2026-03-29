import sys

def solve():
    n = int(sys.stdin.readline())
    w = list(map(int, sys.stdin.readline().split()))
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, sys.stdin.readline().split())
        roads.append((u, v, c))

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][i] = w[i-1]

    for road in roads:
        u, v, c = road
        for k in range(1, n+1):
            if (k != u) and (k != v):
                dp[u][v] = max(dp[u][k] - c + dp[k][v], dp[u][v])

    print(max(dp[i][j] for i in range(1, n+1) for j in range(i+1, n+1)))

solve()
