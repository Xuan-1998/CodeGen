n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n):
    if a[i - 1] == a[i]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = min(dp[i - 2], dp[i - 1])

print(n - dp[n - 1])
