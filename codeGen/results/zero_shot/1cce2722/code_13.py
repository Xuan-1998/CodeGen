import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
for i in range(n):
    dp[i+1] = max(dp[i], a[i])
for i in range(1, n-1):
    for j in range(i):
        if abs(a[j] - a[i]) == 1:
            dp[i+1] = max(dp[i+1], dp[j] + (a[i] not in [a[0], a[-1]]))
print(max(dp))
