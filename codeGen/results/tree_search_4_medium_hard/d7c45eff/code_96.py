dp = [False]*(k+1)
for i in range(1, n+1):
    dp[i] = ((s[i-1] <= s[0]) or dp[i-1])
print(" ".join([c for c in s[:k]]))
