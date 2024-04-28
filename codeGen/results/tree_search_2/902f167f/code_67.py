from collections import defaultdict

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            if i < n and j < m:
                dp[i][j] = min(dp[i - (i // h)][min(j, m)] + (1 if i % h == 0 else 0) for h in range(1, min(i, j) + 1)) + 1
            memo[(i, j)] = dp[i][j]

    return memo[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
