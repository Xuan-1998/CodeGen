def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    dp = [[[[0]* (M+1) for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j][i][j] = 2

    for dx in range(N):
        for dy in range(M):
            for x1 in range(1, N-dx+1):
                for y1 in range(1, M-dy+1):
                    x2, y2 = x1 + dx, y1 + dy
                    dp[x1][y1][x2][y2] %= MOD
                    for x in range(x1, x2):
                        dp[x1][y1][x2][y2] += dp[x1][y1][x][y2] * dp[x+1][y1][x2][y2]
                    for y in range(y1, y2):
                        dp[x1][y1][x2][y2] += dp[x1][y1][x2][y] * dp[x1][y+1][x2][y2]
                    dp[x1][y1][x2][y2] %= MOD
    print(dp[1][1][N][M])

solve()

