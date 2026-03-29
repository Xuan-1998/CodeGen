def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(i ** 0.5)  # largest perfect square less than or equal to i
        for j_val in range(j, 0, -1):  # iterate through all possible j values
            dp[i] = min(dp[i], dp[max(0, i - j_val**2)] + 1)
    return dp[n]

import sys

n = int(sys.stdin.readline())
print(min_perfect_squares(n))
