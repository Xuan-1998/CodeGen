import sys
from math import comb

n = int(input())
s = input()

dp = [[False] * (1 << n) for _ in range(n + 1)]

for i in range(2 ** n):
    for j in range(i, -1, -1):
        if s[j] == '0':
            break
    else:
        continue

    dp[0][i] = True

for i in range(n):
    for j in range(1 << n):
        if (j >> i) & 1 and s[i] == '1':
            dp[n][j ^ (1 << i)] = not dp[n][j]

winning_teams = []
for i in range(1 << n):
    if dp[n][i]:
        winning_teams.append(i)

print(' '.join(map(str, sorted(winning_teams))))
