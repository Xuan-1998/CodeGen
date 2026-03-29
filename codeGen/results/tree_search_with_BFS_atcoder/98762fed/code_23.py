def solve():
    N, M = map(int, input().split())
    mod = 998244353

    two = [1]
    for _ in range(800):
        two.append(two[-1] * 2 % mod)

    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][1] = two[i]
    for i in range(M+1):
        dp[1][i] = two[i]

    for i in range(2, N+1):
        for j in range(2, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + two[i*j-1]
            dp[i][j] %= mod

    print(dp[N][M])

solve()

