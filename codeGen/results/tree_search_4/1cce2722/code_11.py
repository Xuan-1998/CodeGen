def max_points(n, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i - 1] not in a[:i]:
            dp[i] = max(dp[i - 1], (n - i) + dp[min(i, n)] - i)
        else:
            dp[i] = dp[i - 1]
    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(max_points(n, a))
