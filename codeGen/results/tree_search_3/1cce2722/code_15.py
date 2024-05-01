from sys import stdin

n = int(stdin.readline())
max_val = 105
dp = [[0] * (max_val + 1) for _ in range(n + 1)]

for i in range(n + 1):
    a = list(map(int, stdin.readline().split()))
    for k in range(1, max_val + 1):
        if a[i-1] == k:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-1])
        else:
            dp[i][k] = dp[i-1][k]

print(max(dp[n]))
