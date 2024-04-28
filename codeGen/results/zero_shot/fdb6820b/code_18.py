n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in arr:
        if i - j >= 0:
            dp[i] += dp[i - j]
print(dp[-1] % (10**9 + 7))
