def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp_dict = {}

    def memoized_min_squares(i, j):
        if (i, j) not in dp_dict:
            dp_dict[(i, j)] = min(
                1 + memoized_min_squares(i - 1, j),
                1 + memoized_min_squares(i, j - 1)
            )
        return dp_dict[(i, j)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = memoized_min_squares(i, j)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
