def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        m[i][i] = 0

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    def print_order(s, i, j):
        if i == j:
            return str(i)
        else:
            k = s[i][j]
            return '(' + print_order(s, i, k) + ')' + str(i+1) + print_order(s, k+1, j)

    return print_order(s, 0, n-1)

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
