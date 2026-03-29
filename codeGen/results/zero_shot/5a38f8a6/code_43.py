import sys

def min_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for k in range(int(i ** 0.5), -1, -1):
            if k * k <= i:
                dp[i] = min(dp[i], dp[i-k*k] + 1)

    return dp[n]

n = int(input())
print(min_squares(n))
