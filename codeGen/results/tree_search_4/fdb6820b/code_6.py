import sys
from collections import defaultdict

def count_ways(m, N, array):
    MOD = 10**9 + 7
    
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = 1
    for n in range(N + 1):
        if n < 0:
            break
        for i in range(1, m + 1):
            if array[i - 1] > n:
                break
            if array[i - 1] <= n:
                dp[i][n] = (dp[i][n] + dp[i - 1][n - array[i - 1]]) % MOD
    
    return dp[m][N]

m, N = map(int, input().split())
array = list(map(int, input().split()))
print(count_ways(m, N, array))
