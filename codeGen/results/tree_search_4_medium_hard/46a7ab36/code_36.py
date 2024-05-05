import sys

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    mod = 10**8 + 7
    
    dp = [[0] * (m+1) for _ in range(n)]
    
    # Initialize the base case for words of length 0
    dp[0][0] = 1
    
    for i in range(1, n):
        for j in range(m):
            if i < k: 
                dp[i][j] = (dp[i][j] + 1) % mod
            elif 2*i > n or j == m-1:
                dp[i][j] = (dp[i][j] + 1) % mod
            else: 
                for k in range(2*i, n):
                    if i < k and j+1 <= m:
                        dp[i][j] = (dp[i][j] + n * (dp[(i+k)%n][j-1]) % mod)
    
    print(dp[n-1][m-1])
