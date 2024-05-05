===BEGIN PLAN===
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    for j in range(i+1, n+1):
        dp[j] |= (1 << int(s[i]))
maxValue = 0
for i in range(n+1):
    maxValue = max(maxValue, dp[i])
print(format(bin(maxValue)[2:]).zfill(n))
===END PLAN===
