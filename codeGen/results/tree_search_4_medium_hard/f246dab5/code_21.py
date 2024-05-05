n = int(input())
dp = [20] + [0]*(n-1)
for i in range(1, n):
    for j in range(max(0, i-89), i):
        dp[i] = min(dp[i], dp[j-1] + 50 if j > 0 else 50)
    dp[i] = min(dp[i], dp[i-1] + 20)

print(*dp)
