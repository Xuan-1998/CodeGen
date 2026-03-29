import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]
    order = ['A' for _ in range(n-1)]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    order[i:j] = ['(' + c + ')' for c in order[i:k+1]] + [order[k]]

    return ''.join(order)

# Test the function
n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
