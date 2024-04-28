def max_points(n):
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    for i in range(2, n+1):
        if a[i-1] - 1 > 0 and a[i-1] + 1 < a[0]:
            dp[i] = min(dp[i-1], dp[i-2])
        else:
            dp[i] = dp[i-1]
    return n - dp[n]

n = int(input())
print(max_points(n))
