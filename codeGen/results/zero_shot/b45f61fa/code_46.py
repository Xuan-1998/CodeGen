def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n-1]

# Read the input from stdin
n = int(input())
p = [int(x) for x in input().split()]

print(matrix_chain_order(p))
