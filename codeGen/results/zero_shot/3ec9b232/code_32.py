import sys

n = int(input())
M = list(map(int, input().split()))
mod = 10**9 + 7

dp = [0]*n
dp[0] = 1

for i in range(1, n):
    for j in range(i+1):
        if M[j] == i+1:
            dp[i] += dp[j]
    dp[i] %= mod

print(dp[n-1])
