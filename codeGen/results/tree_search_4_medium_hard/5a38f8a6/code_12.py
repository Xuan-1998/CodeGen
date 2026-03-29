import math

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        val = i ** 2
        for j in range(val, 0, -1):
            if j + i ** 2 <= n:
                dp[j] = min(dp[j], dp[i ** 2 - j] + 1)
    return dp[n]

n = int(input())
print(min_perfect_squares(n))
