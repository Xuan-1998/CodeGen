n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if a[i - 1] % 2 == 0:
        dp[i] = dp[i - 1] + a[i - 1] - 1
    else:
        dp[i] = dp[i - 1]
print(dp[-1])
