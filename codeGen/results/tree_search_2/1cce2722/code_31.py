n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    if a[i] == a[0] + 1 or a[i] == a[0] - 1:
        dp[i + 1] = min(dp[i], dp[i - 1])
    else:
        dp[i + 1] = dp[i]

print(dp[n] - n)
