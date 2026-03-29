def count_arrays(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            if j >= k:
                dp[i][j] = dp[i - 1][k]
            else:
                for x in range(2**k):
                    if (x & ((2**k) - 1)) >= k - j and all(((x >> i) & ((2**k) - 1)) >= k - j - 1 for _ in range(i)):
                        dp[i][j] = (dp[i][j] + dp[i - 1][k - j]) % MOD

    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_arrays(n, k))
