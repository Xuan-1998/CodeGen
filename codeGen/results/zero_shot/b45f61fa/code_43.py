def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    result = ''
    i, j = 1, n
    while j > i:
        if j != n and dp[i][j] == dp[i][j - 1] + p[i - 1] * p[j - 1] * p[j]:
            result += '('
        result += 'A' + str(i)
        if j != n:
            result += '*'
        for k in range(i, j):
            result += '*'
        result += 'A' + str(k + 1)
        if j == i:
            result += ')'
        elif j != n:
            result += ') * '
        i = j + 1
    return result

p = [int(x) for x in input().split()]
print(matrix_chain_order(p))
