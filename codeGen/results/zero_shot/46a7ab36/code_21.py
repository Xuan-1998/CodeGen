import sys

def alien_language(n, m):
    dp = [[0] * (m + 1) for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(1, n):
        if 2 * i <= n:
            for j in range(m + 1):
                if j > 0 and (j == i or (dp[i - 1][j - 1] % (10**8 + 7) != 0)):
                    dp[i][j] = (dp[i - 1][j - 1] * (n - i) // (2 * i)) % (10**8 + 7)
                else:
                    dp[i][j] = (dp[i - 1][j] + (n - i) if j == 0 or (j == i and n > 2*i) else 0) % (10**8 + 7)
        else:
            for j in range(m + 1):
                dp[i][j] = (dp[i - 1][j] + (n - i) if j == 0 or (j == i and n > 2*i) else 0) % (10**8 + 7)
    
    return dp[n-1][m]
