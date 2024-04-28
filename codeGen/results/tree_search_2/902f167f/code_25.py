def min_squares(n, m):
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            else:
                min_squares_required = float('inf')
                for k in range(1, min(i, j) + 1):
                    if i >= k and j >= k:
                        min_squares_required = min(min_squares_required, memo[math.floor((i-k)/k)][math.floor((j-k)/k)]) + 1
                memo[i][j] = min_squares_required

    return memo[n][m]
