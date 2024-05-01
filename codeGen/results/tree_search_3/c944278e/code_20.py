import sys

n = int(input())
s = input()

dp = [[False] * (n + 1) for _ in range(2 ** n)]

for i in range(n):
    for j in range(2 ** n):
        if s[i] == '1' and ((j >> i) & 1):
            dp[j][i] = True

winning_teams = []
for j in range(2 ** n):
    won_round = False
    for i in range(n):
        if dp[j][i]:
            won_round = True
            break
    if won_round:
        winning_teams.append(j)

print(*sorted(winning_teams), sep='\n')
