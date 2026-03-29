from sys import stdin

n = int(stdin.readline())
marks = list(map(int, stdin.readline().split()))
pre_sum = [0] * (n + 1)
for i in range(1, n + 1):
    pre_sum[i] = pre_sum[i - 1] + marks[i - 1]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = min(dp[j - 1] + pre_sum[i] - pre_sum[j] for j in range(1, i) if marks[j - 1] < j)

print(dp[n])
