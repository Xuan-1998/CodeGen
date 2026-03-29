def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    # Initialize base case
    for i in range(n):
        dp[i][i] = 0

    # Fill up the table using dynamic programming
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    # Construct the optimal parenthesization
    s = ""
    i, j = 0, n-1
    while i < j:
        min_val = float('inf')
        for k in range(i, j):
            val = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
            if val < min_val:
                min_val = val
                k_opt = k
        s += "("
        for l in range(i, k_opt+1):
            s += "A" + str(l)
            if l < k_opt:
                s += "*"
        s += ")"
        i = k_opt + 1
        j = n-2
    return s
