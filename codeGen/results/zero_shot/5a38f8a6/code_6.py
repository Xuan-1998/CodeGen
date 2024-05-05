import sys

def min_perfect_squares(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        j = int(i ** 0.5)
        min_count = float('inf')
        for k in range(j, -1, -1):
            if k ** 2 <= i:
                min_count = min(min_count, dp[i - k ** 2] + 1)
        dp[i] = min_count
    return dp[n]

n = int(input())
print(min_perfect_squares(n))
