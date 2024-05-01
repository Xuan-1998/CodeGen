===BEGIN PLAN===
n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(n + 1):
    if i == 0:
        dp[i] = a[0]
    else:
        dp[i] = max(dp[i-1], 0) + (a[i] - 1) * min(dp[i//2 - 1] if i % 2 else dp[(i+1)//2 - 1], 0)
print(dp[-1])
===END PLAN===
