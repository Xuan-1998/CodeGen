def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    s = ''
    i, j = n - 1, 0
    while j >= 0:
        if j == i:
            s += 'A'
            i -= 1
        else:
            s += '('
            s += 'A' * (i - j)
            s += ')'
            i -= 1

    return s[::-1]

p = list(map(int, input().split()))
print(matrix_chain_order(p))
