n = int(input())
dp = [0] * n
for i in range(n):
    if i > 0:
        dp[i] = max(dp[i-1], (a[i]-1)*2 if a[i]%2==1 else (a[i]-2))
    else:
        dp[i] = 0

print(max(0, dp[-1]))
