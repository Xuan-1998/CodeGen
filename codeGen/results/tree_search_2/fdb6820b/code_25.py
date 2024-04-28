import sys

def count_ways(N, m):
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(m+1)]

    for i in range(1, N+1):
        for j in range(1, min(i+1, m+1)):
            if i < j:
                dp[j][i] = 0
            else:
                dp[j][i] = (dp[j-1][i-1] + sum(dp[k][i-j] for k in range(j))) % MOD

    return dp[m][N]

# read inputs from standard input
m, N = [int(i) for i in input().split()]
print(count_ways(N, m))
