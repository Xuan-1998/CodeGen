dp = [0] * (n+1)
for i in range(2, n+1):
    if dp[i-1]%2 == 0: # ceiling has an even number of crosses
        dp[i] = min(dp[i-1-p[i-1]] + 1, dp[i-1])  # take the first portal
    else:
        dp[i] = min(dp[i-1-p[i-1]] + 2, dp[i-1]+1)  # take the second portal

print(dp[n+1]%1000000007)
