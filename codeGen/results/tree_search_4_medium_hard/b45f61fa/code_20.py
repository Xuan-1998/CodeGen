def min_cost_matrices(n, p):
    # Initialize memoization table
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # Base case: when i == 0 or k == 0, cost is 0
    def memoized_transition(i, j, k):
        if j - i == 1:
            return p[i] * p[j]
        elif i > 0 and k > 0:
            min_cost = float('inf')
            for split_index in range(i, j):
                cost_left = memoized_transition(i, split_index, k - 1)
                cost_right = memoized_transition(split_index + 1, j, k - 1)
                min_cost = min(min_cost, cost_left + p[i] * p[split_index] * p[j])
            return min_cost
        else:
            return 0

    # Fill up the memoization table
    for i in range(1, n):
        dp[i][i] = 0
        for k in range(1, n - i):
            for j in range(i + k, n):
                dp[i][j] = min_cost_matrices_dp[i][j]

    # Return the minimum cost to multiply all matrices
    return dp[0][n - 1]
