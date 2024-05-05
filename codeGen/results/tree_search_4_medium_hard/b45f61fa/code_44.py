def min_multiplications(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n-1):
        m[i][i] = 0

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    # Reconstruct the optimal parenthesization
    s = []
    i, j = 0, n-1
    while i < j:
        if p[i] * p[i+1] * p[j] == m[i][j]:
            s.append(str(i))
            i += 1
        elif p[k] * p[i] * p[j] == m[i][k] + m[k+1][j]:
            s.append('(')
            s.append(str(k))
            j = k
        else:
            s.append(')')
            j -= 1

    return ''.join(['(', 'A'][i], '* '.join(s), ')']

# Example usage
p = [2, 3, 4]
print(min_multiplications(p))  # Output: ((2*3)*4)
