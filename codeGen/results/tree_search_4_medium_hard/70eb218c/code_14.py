def min_operations(n, x):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for d in range(10):
            if int(x / 10**i) % 10 == d:
                dp[i] = min(dp[i], dp[i-1] + 1)

    return -1 if dp[n] == float('inf') else dp[n]

n, x = map(int, input().split())
print(min_operations(n, x))
