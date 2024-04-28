def max_points_earned():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    points = 0

    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if a[j] == a[i]:
                dp[i][j] = dp[j-1][j-1] + 1
            elif a[j] == a[i]-1:
                dp[i][j] = dp[j-1][j-1] + 1
            else:
                dp[i][j] = max(dp[k-1][j-1] + 1 for k in range(j+1, i+1) if a[k] == a[j] or a[k] == a[j]-1)
            points = max(points, dp[i][j])

    return points

print(max_points_earned())
