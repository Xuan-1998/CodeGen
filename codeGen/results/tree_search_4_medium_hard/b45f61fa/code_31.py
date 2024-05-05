def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(2, n+1):
        m[i][i] = 0

    for L in range(2, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    s = ""
    i = 1
    j = n
    while j > 0:
        k = m[i][j]
        for l in range(p[i-1], p[j]):
            s += str(l)
            if j - i == 1:
                break
            if i+1 <= j-p[i]:
                if m[i+1][i+p[i]-1] + p[i]*p[i+1]*p[l] < m[i+1][j-1] + p[i+1]*p[j-p[i]]*p[l]:
                    s += '('
            else:
                s += ')'
            i = i + 1
        j -= p[i]
    return s

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
