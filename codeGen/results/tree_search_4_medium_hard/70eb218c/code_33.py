def min_operations(n, x):
    dp = [-1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = -1

        for j in range(i):
            if x // 10**j == 0:
                dp[i] = min(dp[i], dp[j-1] + 1)
            else:
                dp[i] = min(dp[i], dp[j-1] + (i - j) + (x // 10**j != 0))

    return dp[n]

n, x = map(int, input().split())
print(min_operations(n, x))
