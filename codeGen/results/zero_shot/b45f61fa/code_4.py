def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    s = ['' for _ in range(n)]
    
    def print_matrix_order(i, j):
        if i == j:
            return 'A' + str(i)
        else:
            min_split_index = i
            min_split_value = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                if q < min_split_value:
                    min_split_index = k
                    min_split_value = q
            s[min_split_index] = '('
            result = print_matrix_order(i, min_split_index) + print_matrix_order(min_split_index + 1, j) + ')'
            return result
    
    return print_matrix_order(0, n - 1)

p = list(map(int, input().split()))
print(matrix_chain_order(p))
