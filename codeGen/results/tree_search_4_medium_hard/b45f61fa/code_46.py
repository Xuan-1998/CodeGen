import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[float('inf')] * (n) for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
    
    for chain_len in range(2, n+1):
        for i in range(n-chain_len+1):
            j = i + chain_len - 1
            for k in range(i+1, j+1):
                dp[i][j] = min(dp[i][j], dp[i][k-1] + p[i]*p[k]*p[j])
    
    return dp[0][n-1]

# Read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# Calculate and print the result
result = matrix_chain_order(p)
print(result)
