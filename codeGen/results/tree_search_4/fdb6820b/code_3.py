import sys

def count_ways(m, N, array):
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, N + 1):
            if j >= array[i - 1]:
                for k in range(i):
                    dp[i][j] += dp[k][j - array[i - 1]]
                dp[i][j] %= MOD
            else:
                dp[i][j] = 0
    
    return dp[m][N]

m, N = map(int, input().split())
array = list(map(int, input().split()))
print(count_ways(m, N, array))
