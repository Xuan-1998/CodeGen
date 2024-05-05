import sys

# Read input and initialize dp table
t = int(input())
mod = 10**9 + 7

dp = [[0] * (10**9 + 7) for _ in range(2*10**5 + 1)]

for i in range(t):
    n, m = map(int, input().split())
    
    # Initialize the dp table
    for j in range(n+1):
        if j == 0:
            dp[0][j] = 1
        else:
            dp[0][j] = (dp[0][j-1] + len(str(j))) % mod
    
    # Fill up the dp table using memoization
    for i in range(1, m+1):
        for j in range(n+1):
            if j == 0:
                dp[i][j] = dp[i-1][0]
            else:
                dp[i][j] = (dp[i-1][j-1] + len(str(j))) % mod
    
    # Print the final answer
    print(dp[m][n], flush=True)
