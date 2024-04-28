def min_falling_path(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    def recurse(i, j):
        if i == 0:  # base case: top row
            return grid[i][j]
        if dp[i][j]:  # memoization: already calculated this subproblem
            return dp[i][j]

        min_val = float('inf')
        for k in range(n):  # consider all columns in the current row
            if i > 0:
                min_val = min(min_val, recurse(i-1, k) + grid[i][j])
            else:  # only consider this column if we're at the top row
                min_val = min(min_val, grid[i][j])

        dp[i][j] = min_val  # store the result in the memoization table
        return dp[i][j]

    return sum(recurse(i, j) for i, j in zip(range(m), range(n)))
