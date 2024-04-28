def max_points(n, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = max(dp[j - 1] + (a[i] - 1) for j in range(1, i + 1))
        else:
            dp[i] = max(dp[j - 1] + 1 for j in range(1, i + 1))
    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(max_points(n, a))
