def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]

def multiply_matrices(p):
    n = len(p) - 1
    s = ['A' for _ in range(n)]
    
    i = 0
    j = n-1
    while j > 0:
        if m[i][j] == m[i][j-1]:
            j -= 1
        else:
            i += 1
            j -= 1
    
    result = ''
    for i in range(n):
        if s[i] != 'A':
            result += '(' + str(s[i])
    
    return result

def main():
    n = int(input())
    p = list(map(int, input().split()))
    
    m = matrix_chain_order(p)
    print(multiply_matrices(p))

if __name__ == "__main__":
    main()
