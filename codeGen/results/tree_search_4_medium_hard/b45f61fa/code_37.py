def matrix_chain_order(p):
    n = len(p) - 1

    # Create a table to store the minimum number of multiplications needed
    dp = [[[0, []] for _ in range(n+1)] for _ in range(n+1)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j][0] = float('inf')
            for k in range(i, j):
                cost = p[i]*p[k+1]*p[j]
                if dp[i][k][0] + cost < dp[i][j][0]:
                    dp[i][j][0] = dp[i][k][0] + cost
                    dp[i][j][1] = [i, k+1] + dp[i][k][1]

    return dp[0][n-1][1]

p = list(map(int, input().split()))
print(*matrix_chain_order(p))
