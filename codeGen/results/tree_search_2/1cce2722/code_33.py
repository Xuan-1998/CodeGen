def max_points(n, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i - 1] == i:
            dp[i] = min(dp[i - 2], 1) if i >= 2 else 1
        else:
            dp[i] = min(dp[i - 1], dp[i - 2]) + 1 if i >= 2 else 1
    return n - dp[n]

n = int(input())
a = list(map(int, input().split()))
print(max_points(n, a))
