===BEGIN CODE===
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = min(dp[p-1] + 1 if p % 2 else dp[p-1]) 
print(dp[n])
