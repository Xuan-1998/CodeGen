import sys

def count_ways(n):
    MOD = 10**9 + 7
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(min(i, n)+1):
            for k in range(j+1):
                if i-k-1 >= 0:
                    dp[i][j] += dp[k][min(j, k)] * dp[i-k-1][min(n-j-1, n-k-1)]
            dp[i][j] %= MOD
    
    return dp[n][0]

n = int(input())
print(count_ways(n))
