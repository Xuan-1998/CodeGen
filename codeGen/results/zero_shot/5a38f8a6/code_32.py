import sys
from math import sqrt

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, int(sqrt(i)) + 1):
            if i - j*j >= 0 and dp[i-j*j] + 1 < dp[i]:
                dp[i] = dp[i-j*j] + 1

    return dp[n]

n = int(input())
print(min_perfect_squares(n))
