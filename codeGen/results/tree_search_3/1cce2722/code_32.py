n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (2 * n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, min(i, n - i) + 1):
        if a[i-1] != k:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k+1])
        else:
            left_points = dp[i-1][k+1]
            right_points = dp[i-1][k-1]
            dp[i][k] = max(left_points, right_points) + 1

print(max(dp[n]))
