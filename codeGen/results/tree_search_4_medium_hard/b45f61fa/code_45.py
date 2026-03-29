from sys import stdin

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize base case: no multiplications needed to multiply a single matrix
    for i in range(n + 1):
        dp[i][i] = 0

    # Fill up the dp table using dynamic programming
    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # Extract the optimal parenthesization from the dp table
    optimal_parenthesization = []
    i, j = 0, n - 1
    while j > i:
        for k in range(i, j):
            if dp[i][k] + dp[k + 1][j] == dp[i][j]:
                optimal_parenthesization.append('(')
                optimal_parenthesization.extend(['A', str(k), ')'])
                j = k
                break

    return ''.join(optimal_parenthesization)


p = [int(x) for x in stdin.readline().split()]
print(matrix_chain_order(p))
