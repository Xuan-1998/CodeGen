import sys

def count_ways(m, N):
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(m+1)]
    
    for j in range(m+1):
        dp[j][0] = 1
    
    for i in range(1, N+1):
        for j in range(1, m+1):
            if i >= arr[j-1]:
                dp[j][i] = (dp[j][i-arr[j-1]] + dp[j-1][i]) % MOD
            else:
                dp[j][i] = dp[j-1][i]
    
    return dp[m][N]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(m, N))
