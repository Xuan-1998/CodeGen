import sys

def solve():
    n = int(input())
    M = list(map(int, input().split()))
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for j in range(n+1):
        dp[0][j] = 1
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            if M[j-1] <= M[i-1]:
                dp[i][j] = (dp[i-1][j-1] + sum(dp[k][j-1] for k in range(i))) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][n]

print(solve())
