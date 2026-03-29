n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + a[i - 1]
    if i > 1:
        dp[i][1] = dp[i - 2][0] + c[i - 1]

print(dp[n][0])
