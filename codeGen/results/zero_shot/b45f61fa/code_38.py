def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # Initialize the base case (i, j)th entry of m to p[i]*p[i+1]
    for i in range(n):
        m[i][i] = p[i] * p[i+1]
        
    # Fill up the rest of the table
    for chain_length in range(2, n+1):
        for start_index in range(n-chain_length+1):
            end_index = start_index + chain_length - 1
            m[start_index][end_index] = float('inf')
            for i in range(start_index, end_index):
                m[start_index][end_index] = min(m[start_index][end_index], 
                                                  m[start_index][i] + m[i+1][end_index] + p[start_index]*p[i+1]*p[end_index+1])
                
    # The minimum number of multiplications is stored in m[0][n-1]
    return m[0][n-1]

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

print(matrix_chain_order(p))
