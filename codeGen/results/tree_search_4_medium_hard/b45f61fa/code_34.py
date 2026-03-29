def minMultiplications(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    # Base case: initialize the first row and column
    for i in range(n):
        dp[i][i] = p[i]**2

    # Fill up the 2D array using dynamic programming
    for chain_len in range(3, n+1):
        for i in range(n-chain_len+1):
            j = i + chain_len - 1
            min_cost = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if cost < min_cost:
                    min_cost = cost
                    dp[i][j] = cost
    # The minimum number of multiplications is stored in dp[0][n-1]
    return str(dp[0][n-1])

# Example usage
import sys
n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(minMultiplications(p))
