import sys

def alien_language(n, m):
    dp = [[0] * (m + 1) for _ in range(n)]
    
    # Initialize first row
    for i in range(2, n+1, 2):
        dp[i][1] = n
    
    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = 1
            else:
                if i % 2 == 0:  # even index
                    dp[i][j] = min(n, dp[(i-1)%n][j-1] * n)
                else:  # odd index
                    dp[i][j] = dp[(i-1)%n][j-1] * n
    
    return pow(dp[-1][-1], -1, 10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
