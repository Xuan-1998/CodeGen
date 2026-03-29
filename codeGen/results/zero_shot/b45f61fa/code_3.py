import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j])

    return dp[0][n-1]

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

result = matrix_chain_order(p)
print(result)
