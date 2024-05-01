def min_tiles(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            dp[i][j] = min((i // k) * ((j // k) if k > 0 else 1) + (dp[i - k][j] if i >= k else 0) + (dp[i][j - k] if j >= k else 0) for k in range(1, min(i, j) + 1))

    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

print(min_tiles(n, m))
