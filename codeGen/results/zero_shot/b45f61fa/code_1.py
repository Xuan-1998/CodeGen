def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    # Initialize the table
    for i in range(n):
        dp[i][i] = 0

    # Fill in the table
    for chain_len in range(2, n+1):
        for i in range(n-chain_len+1):
            j = i + chain_len - 1
            min_cost = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if cost < min_cost:
                    min_cost = cost
            dp[i][j] = min_cost

    # Find the optimal solution
    min_cost = float('inf')
    for j in range(n-1):
        cost = dp[0][j] + p[0]*p[1]*p[j]
        if cost < min_cost:
            min_cost = cost
    return min_cost

# Example usage:
n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
