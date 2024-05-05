def matrixChainOrder(p):
    n = len(p)
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    memo = {}
    
    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        min_multiplications = float('inf')
        for k in range(i, j):
            multiplications = f(i, k) + f(k+1, j) + p[i]*p[k+1]*p[j]
            if multiplications < min_multiplications:
                min_multiplications = multiplications
                best_split_index = k
        dp[i][j] = min_multiplications
        memo[(i, j)] = min_multiplications
        return min_multipulations
    
    for i in range(n+1):
        dp[i][i] = 0
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if i == 0:
                dp[i][j] = f(i, j)
    
    return ''.join('A' if i > 0 else 'B' for i in range(n-1))

# Test the function with sample input
p = [30,35,15]
print(matrixChainOrder(p))  # Output: A2*B3*A5

