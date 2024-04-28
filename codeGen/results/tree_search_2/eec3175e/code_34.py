def is_divisible(n, m):
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i):
            if (i - j) % m == 0:
                dp[i] = dp[i] or dp[j]

    return dp[n]


n, m = map(int, input().split())
print(int(is_divisible(n, m)))
