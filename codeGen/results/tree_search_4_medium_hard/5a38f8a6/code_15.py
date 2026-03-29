import sys

def min_perfect_squares(n):
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(int(i ** 0.5) + 1):
            if i >= j * j:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
    return dp[n]

n = int(input())
print(min_perfect_squares(n))
