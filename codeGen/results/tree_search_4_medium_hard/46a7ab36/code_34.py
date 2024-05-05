import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mod = 10**9 + 7
    
    # Initialize dp table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: single letter words
    for i in range(n):
        dp[i][1] = 1

    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(2 * i + 1): 
            if j == 1:
                dp[i][j] += dp[i - 1][0]
            else:
                dp[i][j] += dp[i - 1][j - 1]
    
    # Calculate the total number of possible words
    ans = dp[n][m]
    print(ans % mod)
