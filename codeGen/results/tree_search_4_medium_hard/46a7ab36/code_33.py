import sys

def alien_language(n, m):
    MOD = 10**8 + 7
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: single character words
    for i in range(1, n + 1):
        if i * 2 <= n:
            dp[i][1] = MOD
    
    # Fill up the dynamic programming table
    for j in range(2, m + 1):
        for i in range(1, min(n, j // 2) + 1):
            if j % 2 == 0:
                dp[i][j] += dp[i][j - 1]
            else:
                dp[i][j] += dp[min(i, n - (j - 1))][j - 1]
            dp[i][j] %= MOD
    
    # Calculate the total number of possible words
    ans = sum(dp[0][i] for i in range(m + 1))
    return int(ans % MOD)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
