import math

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if j ** 2 <= i:
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])

    return dp[n]

n = int(input())
print(min_perfect_squares(n))
