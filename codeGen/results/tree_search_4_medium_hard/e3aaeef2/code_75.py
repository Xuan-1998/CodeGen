import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(11)]
    
    # base case: after 0 operations, the length is the same as the initial number
    dp[1][0] = 1
    
    for i in range(2, 11):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = i
            else:
                dp[i][j] = (dp[i-1][j-1] + len(str(i)) - 1) % MOD
    
    print(dp[10][m])
