code
n = int(input())
M = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1

for m in M:
    for i in range(n, m - 1, -1):
        dp[i] += dp[i - m]
    dp[m] %= (10**9 + 7)

print(dp[n])
