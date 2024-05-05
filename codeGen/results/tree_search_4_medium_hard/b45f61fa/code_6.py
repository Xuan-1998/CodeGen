def matrix_chain_order(p):
    n = len(p)
    m = [[0] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            m[i][j] = float('inf')
            for k in range(j, i):
                q = m[k+1][i] + m[j][k] + p[j]*p[k]*p[i]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]

def get_parenthesization(p, m):
    n = len(p)
    s = ['(' for _ in range(n-1)]
    j = 0
    for i in range(2, n+1):
        while m[i][j] != m[i][i-1]:
            j += 1
        s[j] = ')'
        j -= 1
    return ''.join(s)

p = list(map(int, input().split()))
print(get_parenthesization(p, matrix_chain_order(p)))
