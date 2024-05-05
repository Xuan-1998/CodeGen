def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        dp[i][i] = p[i-1] * p[i]
        for j in range(i - 1, 1, -1):
            dp[j][i] = float('inf')
            for k in range(j, i):
                cost = dp[k][j] + p[k] * p[j] * p[i]
                if cost < dp[j][i]:
                    dp[j][i] = cost
    return ''.join(f'Matrix {i+1}' for i in range(n - 1) if p[i] == p[i+1]) + ')'

p = [int(x) for x in input().split()]
print(matrix_chain_order(p))
