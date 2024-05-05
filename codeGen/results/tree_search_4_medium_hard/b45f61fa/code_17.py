def matrix_chain_order(p):
    n = len(p)
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0

    for chain_len in range(2, n+1):
        for i in range(n-chain_len+1):
            j = i + chain_len - 1
            for k in range(i, j+1):
                if k == i:
                    dp[i][j] = min(dp[i][j], p[i]*p[k+1]*dp[k+1][j])
                elif k == j:
                    dp[i][j] = min(dp[i][j], p[i]*p[j+1]*dp[i][k])
                else:
                    dp[i][j] = min(dp[i][j], (p[i]*p[k+1]+p[k+2]*p[j+1])*dp[i][k]+dp[k+1][j])

    order = []
    i, j = n-1, 0
    while i > 0:
        if j < i and dp[j][i] != dp[j][i-1]:
            order.append((chr(ord('A')+j), chr(ord('A')+i)))
            i -= 1
            j -= 1
        else:
            j -= 1

    return '(' + ') * ('.join(map(lambda x: str(x[0])+' '+str(x[1]), order[::-1]))+')'
