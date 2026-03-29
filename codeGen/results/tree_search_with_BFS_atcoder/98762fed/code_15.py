MOD = 998244353

def solve(N, M):
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if i > 0:
                dp[i][j] += 2 * dp[i-1][j]
            if j > 0:
                dp[i][j] += 2 * dp[i][j-1]
            if i > 0 and j > 0:
                dp[i][j] -= dp[i-1][j-1]
            dp[i][j] %= MOD
    return dp[N][M]

N, M = map(int, input().split())
print(solve(N, M))

