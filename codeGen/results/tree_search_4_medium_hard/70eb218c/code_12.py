def min_operations(n, x):
    if n == 1:
        return 0

    dp = [[float('inf')] * 10 for _ in range(n + 1)]
    dp[1] = [0] * 10

    for i in range(2, n + 1):
        for d in range(10):
            if x >= 10 ** (i - 1) and d < 10 ** (n - i):
                return -1
            for y in range(10):
                dp[i][d] = min(dp[i][d], dp[i - 1][y] + (d != 0))

    return dp[n][-1]

import sys

n, x = map(int, input().split())
print(min_operations(n, x))
