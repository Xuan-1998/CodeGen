n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    for k in range(1, i + 1):
        dp[i][k] += max(dp[i-1].max(), i - k)

print(max(dp[n]))
