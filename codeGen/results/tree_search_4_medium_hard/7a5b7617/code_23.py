import sys

def count_stable_tables(N, M):
    MOD = 10**9 + 7
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    # Initialize base case: filling an empty table
    for j in range(M+1):
        dp[0][j] = 1
    
    for i in range(1, N+1):
        for j in range(M+1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = sum(dp[k][M-k] for k in range(i)) % MOD
    
    return dp[N][M]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_stable_tables(N, M))
