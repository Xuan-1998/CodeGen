import sys

n = int(input())
s = input()

dp = [0] * (n + 1)
dp[0] = 2 ** n

for i in range(n):
    if s[i] == '1':
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] // 2

winning_teams = []
for i in range(n, -1, -1):
    if dp[i] > 0:
        winning_teams.append(dp[i])
    if s[i-1] == '1':
        break

print(*winning_teams)
