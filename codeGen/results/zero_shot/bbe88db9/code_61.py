import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1 if i % 2 == 1 else dp[p[i - 1]] + 1

print(dp[-1] % 1000000007)
