import sys

def count_matrices(N):
    dp = [[0]*(N+1) for _ in range(N+1)]
    
    for j in range(N+1):
        dp[0][j] = 1
    
    for i in range(1, N+1):
        for j in range(i+1):
            if i % 2 == 0:
                dp[i][j] += dp[(i-2)//2][j]
            else:
                dp[i][j] += dp[(i-3)//2][j]
    
    return dp[N][N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
