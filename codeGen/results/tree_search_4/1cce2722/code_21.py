def max_points_earned(a):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0 or i == 1:
            dp[i] = sum(a[:i+1])
        else:
            dp[i] = max(dp[i-1], dp[i-2] + a[i] - a[i-1])

    return dp[n]

# Example input
a = list(map(int, input().split()))
print(max_points_earned(a))
