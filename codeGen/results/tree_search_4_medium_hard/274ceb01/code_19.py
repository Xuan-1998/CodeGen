import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [0] * (n + 1)
prev_marks = 0

for i in range(1, n + 1):
    prev_above = dp[i - 1]
    if marks[i - 1] > i:  # more marks above water than previous days
        dp[i] = min(prev_above, prev_marks + marks[i - 1])
    else:
        dp[i] = prev_above + 1
    prev_marks += marks[i - 1]

print(dp[-1])  # minimum possible sum of marks strictly below the water level
