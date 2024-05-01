import sys

def max_points(n):
    a = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(i, -1, -1):
            if k > i:
                dp[i][k] = dp[i-1][k]
            elif a[k-1] == a[i]:
                dp[i][k] = max(dp[i-1][k], dp[i-1][k-2])
            else:
                dp[i][k] = max(dp[i-1][k-1], dp[i-1][k-2]) + 3

    return dp[n][n]

print(max_points(int(input())))
