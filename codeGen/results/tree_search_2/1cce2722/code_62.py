from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

dp = [0] * (n + 2)
for i in range(1, n + 1):
    if a[i - 1] > 0:
        dp[i] = max(dp[i], dp[i - 1])
    else:
        dp[i] = max(dp[i], dp[i - 1] + 1)
    for j in range(i - 2, -1, -1):
        if a[j] == a[i]:
            break
        if a[j] > a[i]:
            break
        dp[i] = max(dp[i], dp[j - 1])
for i in range(n, -1, -1):
    for j in range(i + 2, n + 2):
        if a[i] == a[j]:
            dp[j] = min(dp[j], dp[i] - 1)
print(max(dp))
