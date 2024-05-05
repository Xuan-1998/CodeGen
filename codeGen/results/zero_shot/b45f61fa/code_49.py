def minimal_parentheses(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for chain_length in range(2, n+1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + p[k]*p[k+1]*dp[k+1][j] + p[i]*p[j])
    
    return dp[0][n-1]

# Read input
n = int(input())  # number of matrices
p = list(map(int, input().split()))  # dimensions of matrices

print(minimal_parentheses(p))
