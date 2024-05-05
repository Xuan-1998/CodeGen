def min_perfect_squares(n):
    if n < 2:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

import sys
n = int(input())
print(min_perfect_squares(n))
