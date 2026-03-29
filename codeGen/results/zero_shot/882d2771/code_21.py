import sys

t = int(input())
l, r = map(int, input().split())

dp = [0] * (r + 1)
for i in range(2, r + 1):
    dp[i] = 1 + min(dp[j] + 1 for j in range(1, i))

answer = 0
for i in range(t):
    answer += i * dp[l + i - 1]
answer -= l * dp[r]

print(answer % (10**9 + 7))
