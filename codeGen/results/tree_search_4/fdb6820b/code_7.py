def count_ways(m, N, array):
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(1, m + 1):
        for k in array[:i]:
            for j in range(min(N, k), -1, -1):
                dp[i][j] += 2 * dp[i-1][j-k]
                dp[i][j] %= MOD
            if k <= N:
                dp[i][N] += 1
                dp[i][N] %= MOD

    return dp[m][N]

m = int(input())
N = int(input())
array = [int(x) for x in input().split()]

print(count_ways(m, N, array))
