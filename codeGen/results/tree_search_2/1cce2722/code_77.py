def max_points(n):
    a = list(map(int, input().split()))
    dp = [0] * n

    for i in range(1, n):
        if a[i] == a[i-1]:
            dp[i] = 1 + (dp[i-1] if i > 1 else 0)
        else:
            dp[i] = max(dp[i-1], 1 + (dp[i-2] if i >= 2 else 0))

    return dp[-1]

n = int(input())
print(max_points(n))
