import sys

def alien_language(n, m):
    k = n
    dp = [[0] * (m + 1) for _ in range(k + 1)]
    
    # base case: no letters have been added to the word yet
    dp[0][0] = 1
    
    for j in range(m):
        for i in range(k + 1):
            if j == 0:
                if i < k:
                    dp[i][j] = k - i
                elif i < 2 * n:
                    dp[i][j] = n
                else:
                    dp[i][j] = dp[k-1][m-1]
            else:
                if j == m:
                    if i < k:
                        dp[i][j] += dp[k-1][0]
                    elif i < 2 * n:
                        dp[i][j] = n
                    else:
                        dp[i][j] = dp[k-1][m-j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]
    
    return (dp[k][m] + 7) % (10**8 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
