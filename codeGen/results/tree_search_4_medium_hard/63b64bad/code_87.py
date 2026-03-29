import sys

n = int(input())
dp = [-1] * (2*n+1)
for i in range(1, n+1):
    a_i = int(input())
    for y in range(n, -1, -1):
        if y + a_i > 2*n or y < 0:
            dp[y+a_i] = y
        else:
            dp[y+a_i] = max(dp[y+a_i], y+a_i)
print(max(i for i in range(n+1) if dp[i] != -1))
