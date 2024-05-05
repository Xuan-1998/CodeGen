import sys

t = [int(input()) for _ in range(t)]
l, r = map(int, input().split())

dp = [0] * (r+1)
for i in range(2, r+1):
    dp[i] = dp[i-1] + i - 1

result = t[0] * (dp[l] - l)
for i in range(1, r+1):
    result += t[i] * (dp[l+i] - l - i)

print(result % (10**9 + 7))
