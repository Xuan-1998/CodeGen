from collections import defaultdict

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    s = [['' for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        m[i][i] = 0

    for L in range(2, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = '(' + s[i][k] + s[k+1][j] + ')'
            if i == 1:
                s[i][j] = ''

    return s[1][n-1]

p = [int(x) for x in input().split()]
print(matrix_chain_order(p))
