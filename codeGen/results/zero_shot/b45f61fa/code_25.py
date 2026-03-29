def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if i == j:
                dp[j][i] = p[j] * p[j]
            else:
                dp[j][i] = float('inf')
                for k in range(j, i):
                    dp[j][i] = min(dp[j][i], dp[j][k] + p[k] * p[i])

    result = []
    i, j = 0, n
    while j > 0:
        if i < j and dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            result.append('A' + str(i+1))
            i += 1
            j -= 1

    return ''.join(result[::-1])
