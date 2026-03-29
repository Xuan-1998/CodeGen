def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                m[i][j] = min(m[i][j], q)
    
    s = []
    i, j = 0, n - 1
    while j > 0:
        if m[i][j] == m[i][k] + m[k + 1][j] for k in range(i, j):
            j = k
        elif m[i][j] == m[i][k] + m[k + 1][j] for k in range(j - 1, i, -1):
            i = k + 1
        s.append('A' if i == 0 else 'B')
    return ''.join(s[::-1])
