def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    memo = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                min_cost = float('inf')
                for k in range(i, j + 1):
                    cost = dp[i][k] + dp[k][j] + p[i - 1] * p[k] * p[j]
                    if cost < min_cost:
                        min_cost = cost
                        dp[i][j] = cost
                memo[(i, j)] = dp[i][j]
    
    return memo[(0, n - 1)]

p = list(map(int, input().split()))
print(matrix_chain_order(p))
