import sys

n = int(input())  # read number of days from input
m = list(map(int, input().split()))  # read number of marks strictly above water on each day

dp = [0] * (n + 1)  # initialize dp table with size n+1
ans = 0  # initialize answer variable

for i in range(1, n + 1):
    if i <= m[i-1]:
        dp[i] = 0
    else:
        dp[i] = min(dp[i-1], (i-m[i-1]) * m[i-1])
    ans = min(ans, dp[i])

print(ans)  # print the final answer
