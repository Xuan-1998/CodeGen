def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n+1) for _ in range(n+1)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp

def matrix_chain_parenthesis(p):
    n = len(p) - 1
    dp = matrix_chain_order(p)
    s = ''
    i, j = n-1, 0
    while j > 0:
        if p[i] < p[j]:
            s = 'A' + s
            j -= 1
        else:
            s = '(' + s
            i, j = j, i - 1
    return s

p = list(map(int, input().split()))
print(matrix_chain_parenthesis(p))
