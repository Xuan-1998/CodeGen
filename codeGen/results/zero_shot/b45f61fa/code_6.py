def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]

    # fill up the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q

    # reconstruct the optimal parenthesization
    s = ['(' + str(i) for i in range(n - 1)]
    j = n - 2
    while j > 0:
        for i in range(j, 0, -1):
            if m[i][j] != m[i - 1][j]:
                break
        s.insert(2 * (j + 1), ')')
        j = i - 1

    return ''.join(s).strip('()')

# get input from stdin
n = int(input())
p = list(map(int, input().split()))

print(matrix_chain_order(p))
