import sys
n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + (i - 1), marks[i - 1])
print(min(marks))
