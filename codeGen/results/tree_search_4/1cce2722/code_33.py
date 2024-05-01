from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)
a = list(map(int, stdin.readline().split()))

for i in range(1, n + 1):
    for k in range(i + 1, min(i + a[i - 1], n) + 1):
        dp[i] = max(dp[i], dp[k - 1] + (k - i))

print(dp[n])
