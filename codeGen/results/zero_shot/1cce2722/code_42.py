n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n):
    if a[i - 1] == a[i] and a[i] == a[i + 1]:
        dp[i + 1] = max(dp[i], dp[i - 2] + 3)
    else:
        dp[i + 1] = dp[i]
print(max(dp))
