code
def count_ways(m, N):
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(N // i + 1):
            if i == 1:
                dp[i][j] = j
            else:
                if j >= i:
                    dp[i][j] = (dp[i-1][j-i] + sum(dp[k][j] for k in range(i))) % (10**9 + 7)
                else:
                    dp[i][j] = dp[i-1][j]
    return dp[m][N]

m, N = map(int, input().split())
print(count_ways(m, N) % (10**9 + 7))
