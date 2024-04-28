n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n):
    if i > 1 and abs(a[i-1] - a[i]) == 1:
        dp[i] = min(dp[i-1], dp[i-2]) + 1
    else:
        dp[i] = dp[i-1]

print(n - dp[-1])
