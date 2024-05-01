def find_subset_sum(n, m):
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for j in range(m + 1):
        if not any(dp[k][j % m] for k in range(j)):
            return False

    return True
