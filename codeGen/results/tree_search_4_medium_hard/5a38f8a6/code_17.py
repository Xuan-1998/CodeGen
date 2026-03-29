def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(i ** 0.5)
        while j >= 1:
            if i - j ** 2 >= 0:
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])
            j -= 1

    return dp[n]

import sys
input = sys.stdin.readline
n = int(input())
print(min_perfect_squares(n))
