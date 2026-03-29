def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # fill the m table in a bottom-up manner
    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            if j == i-1:
                m[j][i] = 0
            else:
                min_val = float('inf')
                for k in range(j, i):
                    q = m[j][k] + m[k+1][i] + p[j]*p[k+1]*p[i]
                    if q < min_val:
                        min_val = q
                m[j][i] = min_val
    
    # reconstruct the optimal order from the m table
    s = ['' for _ in range(n)]
    i, j = 0, n-1
    while j > 0:
        if j == i+1:
            s[i] = str(i)
            i -= 1
            j -= 1
        else:
            min_val_idx = -1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    min_val_idx = k
            s[min_val_idx] = '(' + s[min_val_idx] + ')' + s[0]+s[min_val_idx-1]+')' + s[min_val_idx+1]
            i, j = 0, min_val_idx
    
    return ''.join(s)

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
