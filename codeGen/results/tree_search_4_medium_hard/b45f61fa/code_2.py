def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def multiply_matrices(i, j):
        if i == 0 or j == n:
            return 0
        min_multiplications = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[k]
            if q < min_multiplications:
                min_multiplications = q
        return min_multiplications

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = multiply_matrices(i, j)

    # Reconstruct the optimal parenthesization from the dp table
    parentesis_order = []
    i, j = n - 1, 0
    while j < n:
        min_k = j
        for k in range(j + 1, i, -1):
            if dp[i][k - 1] + dp[k][j] < dp[i][min_k]:
                min_k = k
        parentesis_order.append(min_k)
        i, j = min_k, j

    return ''.join(chr(65 + i) for i in reversed(parentesis_order))
