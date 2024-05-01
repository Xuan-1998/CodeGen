import sys

def max_points(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = 1

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if a[j] == a[i] - 1 or a[j] == a[i] + 1:
                dp[i][j] = max(dp[i-1][k] + (n-k) - i for k in range(j))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n-1][-1]


# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

print(max_points(a))
