MOD = 998244353

def solve(N, M):
    dp = [[[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j][i][j] = 2
    for len1 in range(1, N+1):
        for len2 in range(1, M+1):
            for i in range(1, N-len1+2):
                for j in range(1, M-len2+2):
                    k = i + len1 - 1
                    l = j + len2 - 1
                    dp[i][j][k][l] = (dp[i+1][j][k][l] + dp[i][j+1][k][l] - dp[i+1][j+1][k][l] + dp[i][j][k-1][l-1]) % MOD
                    dp[i][j][k][l] = (dp[i][j][k][l] + dp[i][j+1][k][l] - dp[i][j+1][k-1][l] + dp[i+1][j][k][l-1]) % MOD
    return dp[1][1][N][M]

N, M = map(int, input().split())
print(solve(N, M))

