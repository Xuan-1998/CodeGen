import sys

n = int(input())
operations = input()

dp = [0] * (n + 1)
dp[0] = 1  # base case: one stone left after no operations

for i in range(1, n + 1):
    if operations[i - 1] == '-':
        dp[i] = max(dp[i - 1] - 1, 0)  # subtract one stone
    else:
        dp[i] = dp[i - 1] + 1  # add one stone

print(min(dp))  # print the minimal possible number of stones
