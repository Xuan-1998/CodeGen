import sys

def max_grade(n, t):
    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if t % 10 >= 5:
            dp[i] = max(dp[i - 1], int(str(t // 10).zfill(i)))
        else:
            dp[i] = dp[i - 1]

    return dp[n]

n, t = map(int, input().split())
print(max_grade(n, t))
