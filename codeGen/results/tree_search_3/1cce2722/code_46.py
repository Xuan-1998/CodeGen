from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = defaultdict(int)
dp[0] = 0

for i in range(1, n):
    dp[i] = dp[i-1]
    if a[i] - 1 in dp and a[i] + 1 in dp:
        dp[i] += min(dp[a[i]-1], dp[a[i]+1]) + 1
    elif a[i] - 1 in dp:
        dp[i] = max(dp[i], dp[a[i]-1] + 1)
    elif a[i] + 1 in dp:
        dp[i] = max(dp[i], dp[a[i]+1] + 1)

print(max(0, dp[-1]))
