n = int(input())
a = [int(x) for x in input().split()]

dp = [0] * (n + 1)
for i in range(1, n):
    if a[i] != a[i-1] and a[i] != a[i+1]:
        dp[i+1] = max(dp[i]-1, dp[i])
    else:
        dp[i+1] = dp[i]

print(dp[n])
