def subset_sum(d, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - d[i - 1]] + d[i - 1])

    return [i for i in range(0, n + 1) if i != 0 and dp[n][i] == i]

# Example usage
d = [1, 2, 3]
n = len(d)
print(" ".join(map(str, subset_sum(d, n))))
