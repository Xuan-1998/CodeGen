import math
from collections import defaultdict

def max_grade(n, t):
    dp = [[0] * (t + 1) for _ in range(n + 1)]

    # Initialize the base case: no digits after the decimal point
    for j in range(t + 1):
        dp[0][j] = 0

    memo = defaultdict(int)

    def dfs(i, j):
        if i > n or j < 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        # If we can't fit the current digit within the time limit,
        # just consider the previous maximum possible grade
        if j - 1 < 0:
            result = dp[i-1][j]
        else:
            # Consider two options: round up or not round at all
            if i > 1 and (i % 10 == 4 or i % 10 in [6,8]):
                result = max(dfs(i - 1, j - 1) + 1, dp[i-1][j])
            else:
                result = max(dfs(i - 1, j), dp[i-1][j])

        memo[(i, j)] = result
        return result

    return dfs(n, t)

n, t = map(int, input().split())
print(max_grade(n, t))
