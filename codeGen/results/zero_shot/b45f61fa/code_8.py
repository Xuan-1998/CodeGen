def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = 0

    for L in range(2, n + 1):
        for i in range(1, n - L + 3):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
    s = ''
    i, j = 1, n
    while j > i:
        if p[i] >= p[j]:
            s += 'A'
            j -= 1
        else:
            s += 'B'
            i += 1

    return s
