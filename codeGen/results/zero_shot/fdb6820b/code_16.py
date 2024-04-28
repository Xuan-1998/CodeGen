m, n = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1
for x in arr:
    for i in range(n, x - 1, -1):
        dp[i] += dp[i - x]
print(dp[n] % (10**9 + 7))
