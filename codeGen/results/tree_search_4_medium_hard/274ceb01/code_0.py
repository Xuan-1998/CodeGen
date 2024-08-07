import sys

n = int(sys.stdin.readline())
marks = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = min(dp[i - 1], marks[i - 1])
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + marks[i - 1] - marks[j])

print(min(dp))
