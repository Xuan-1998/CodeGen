def maximum_points(n):
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)

    for i in range(2, n):
        max_points = 0
        for j in range(i - 1):
            if abs(a[i] - a[j]) == 1:
                max_points = max(max_points, dp[j])
        dp[i] = dp[i - 1] + max_points

    return dp[-1]

n = int(input())
print(maximum_points(n))
