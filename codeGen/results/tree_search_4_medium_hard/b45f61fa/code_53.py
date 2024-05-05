def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    result = ''
    i, j = n - 1, 0
    while i > 0:
        if j == 0:
            i -= 1
        elif j == i:
            result += 'A'
            i -= 1
        else:
            result += '('
            for k in range(i, j):
                result += 'A' + str(k + 1) + ', '
            result = result[:-2] + ')'
            j = i
    return result

p = list(map(int, input().split()))
print(matrix_chain_order(p))
