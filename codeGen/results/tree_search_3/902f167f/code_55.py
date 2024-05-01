def min_tiles(n, m):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return 0

        min_squares = float('inf')

        for k in range(1, min(i, j) + 1):
            remaining_i = i - k
            remaining_j = j - k
            if (remaining_i, remaining_j) not in memo:
                memo[(remaining_i, remaining_j)] = dp(remaining_i, remaining_j)
            min_squares = min(min_squares, dp(remaining_i, remaining_j) + 1)

        memo[(i, j)] = min_squares
        return min_squares

    return dp(n, m)

n, m = map(int, input().split())
print(min_tiles(n, m))
