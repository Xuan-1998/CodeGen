def matrix_chain_order(p):
    n = len(p) - 1

    # Step 2-4: Fill up the DP Table and reconstruct the optimal parenthesization
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[''] * (n + 1) for _ in range(n + 1)]

    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = p[i] * p[k+1] * p[j]
                cost = dp[i][k] + dp[k+1][j] + q
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = '(' + s[i][k] + 'A' + str(k) + '*' + str(p[k]) + 'B' + str(j-k) + ')' + 'C'
            dp[i][j] += q

    # Step 5: Print the optimal parenthesization
    return s[0][n-1]

p = [30, 35, 15]
print(matrix_chain_order(p))
