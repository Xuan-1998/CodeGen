n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for s in range(2, n + 1):
    if a[s - 1] == a[0] or a[s - 1] - 1 == a[0]:
        dp[s] = max(dp[max(0, s - 2)] + s, dp[max(0, s - 1)] + 1)
    else:
        dp[s] = dp[max(0, s - 1)] + 1

print(dp[n])
