def max_sum_path(tree):
    n = len(tree)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        parent = tree[i - 1]
        left = right = 0

        if 2 * i <= n:
            left = dp[2 * i]

        if 2 * i + 1 <= n:
            right = dp[2 * i + 1]

        dp[i] = max(parent, parent + left + right)

    return dp[n]
