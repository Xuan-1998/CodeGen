def min_cost(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):
        dp[i][i-1] = p[0] * p[i]

    for chain_length in range(2, n):
        for start in range(n - chain_length):
            end = start + chain_length
            min_cost = float('inf')
            for split_index in range(start, end):
                cost = dp[start][split_index-1] + p[split_index]*p[split_index+1]*p[end]
                if cost < min_cost:
                    min_cost = cost
                    dp[start][end-1] = cost
    return dp[0][n-2]

# Example usage:
p = [5, 3, 1, 4, 7, 2, 6]
print(min_cost(p))
