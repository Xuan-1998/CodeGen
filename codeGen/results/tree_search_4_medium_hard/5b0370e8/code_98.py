def solution():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = (dp[i-1][j] * (2**k - 2**(k-j)) % MOD) if i > 0 else 1
                elif i > 0 and j < k:
                    dp[i][j] = (sum(dp[m][j-1] * (2**k - 2**(k-(j-1))) % MOD for m in range(i+1)) + dp[i][j-1]) % MOD
        print((dp[n][k] - 1) % MOD)

solution()
