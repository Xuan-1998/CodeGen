def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    def place_square(i, j):
        if i < j:
            return 0
        if i == j:
            return 1
        min_squares = float('inf')
        for k in range(1, min(i, j) + 1):
            remaining_i, remaining_j = i - k, j - k
            if dp[remaining_i][remaining_j] != float('inf'):
                min_squares = min(min_squares, 1 + dp[remaining_i][remaining_j])
        return min_squares

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = place_square(i, j)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
