import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (10**9 + 7) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1 if i == 0 else 0

for j in range(1, 10**9 + 7):
    for i in range(n, -1, -1):
        for k in range(i):
            if m[k] in m and j >= m[k]:
                dp[i][j] += dp[k][j - m[k]]
                dp[i][j] %= (10**9 + 7)

print(dp[n][-1])
