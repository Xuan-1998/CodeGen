n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(1, n):
    dp[i][0] = max(a[i - 1], c[i - 1])
    dp[i][1] = max(b[i - 1], a[i])

dp[n][0] = max(a[-1], c[-1])
print(max(dp[n][0], dp[n][1]))
