import sys

def count_ways(m, n, arr):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - arr[i - 1]]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[m][n]

m, n = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(m, n, arr))
