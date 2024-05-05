import sys

n = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(1, (i - 1) // 60) * 20
    dp[i][1] = min(i - 90, n) if i >= 90 else 0
    dp[i][1] += (min(i - 90, n) >= i ? (i - min(i-90, n)) : 0) * 50
    dp[i][2] = min(i - 14 * 60, n) if i >= 14 * 60 else 0
    dp[i][2] += (min(i - 14 * 60, n) >= i ? (i - min(i-14*60, n)) : 0) * 120

for i in range(n + 1):
    print(dp[i][2])
