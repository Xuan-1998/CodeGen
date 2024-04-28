n, k = map(int, input().split())
dp = [1] * (k + 1)
for i in range(2, n + 1):
    for j in range(min(i, k), 0, -1):
        if i % j == 0:
            dp[j] = (dp[j] * i) % 1000000007
print(dp[k])
