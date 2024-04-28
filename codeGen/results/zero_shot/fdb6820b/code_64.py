n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n+1):
    for j in range(m):
        dp[i] = (dp[i] + dp[i-a[j]]) % (10**9 + 7)

print(dp[n])
