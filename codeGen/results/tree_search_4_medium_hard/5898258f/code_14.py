from collections import defaultdict

def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [[-float('inf')] * ((N + X) // 2 + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        for j in range(min(i, (N + X) // 2)):
            if j == 0 or i == 1:
                dp[i][j] = A[0] ^ A[i - 1]
            else:
                for k in range(j + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] ^ A[i - 1] ^ A[i])
    
    return max(dp[N])

print(solve())
