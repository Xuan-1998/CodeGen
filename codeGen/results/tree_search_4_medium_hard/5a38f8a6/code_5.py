from math import sqrt

def min_perfect_squares(n):
    dp = [float('inf')] * (int(sqrt(n)) + 1)
    dp[0] = 0
    for i in range(1, int(sqrt(n)) + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[-1]

n = int(input())
print(min_perfect_squares(n))
