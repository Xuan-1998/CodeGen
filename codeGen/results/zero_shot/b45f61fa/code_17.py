def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    s = []
    i, j = 1, n
    while j > i:
        for k in range(i, j):
            if m[i][k] + m[k + 1][j] == m[i][j]:
                s.append(chr(ord('A') + k))
        j -= (m[i][j - 1] - m[i][j]) // p[j]
        i = j

    return "".join(s)
