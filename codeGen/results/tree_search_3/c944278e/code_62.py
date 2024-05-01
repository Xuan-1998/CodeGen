import sys

n = int(input())
s = input()

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(2 ** (i - 1)):
        if s[j] == 'W':
            dp[i][0] += 1
        else:
            dp[i][1] += 1

winning_teams = []
for k in [0, 1]:
    temp_team_count = dp[n][k]
    for i in range(n - 1, -1, -1):
        if s[dp[i - 1][int(not k)]] == str(int(not k)):
            temp_team_count += dp[i - 1][k]
    winning_teams.append(temp_team_count)

print(*sorted(winning_teams), sep='\n')
