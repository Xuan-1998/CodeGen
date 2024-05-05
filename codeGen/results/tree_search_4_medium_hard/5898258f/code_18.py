import sys

def max_xor_sum(N, X):
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(min(i - 1, X) + 1):
            if j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (A[i-1] ^ A[i]))
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[N][X]

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(N, X))
