def solve():
    T = int(input())
    MOD = 10**9 + 7

    dp = [[0] * (2001) for _ in range(2001)]
    dp[0] = [1] * 2001

    for i in range(N):
        for j in range(M):
            for k in range(i+1):
                if j + k <= M:
                    dp[i][j] += dp[k-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N-1][M])
