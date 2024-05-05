import math

def minPerfectSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            if dp[i - j * j] + 1 < dp[i]:
                dp[i] = dp[i - j * j] + 1
            j += 1

    return dp[n]

n = int(input())
print(minPerfectSquares(n))
