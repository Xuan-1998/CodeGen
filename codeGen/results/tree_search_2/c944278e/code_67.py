import sys

n = int(input())
s = input()

dp = [[[] for _ in range(n + 1)] for _ in range(1 << n)]

for i in range(1 << n):
    for j in range(n, -1, -1):
        if (i >> j) & 1:
            dp[i][j] = [x for x in dp[i ^ (1 << j)][j - 1] if x not in dp[i][j - 1]]
        else:
            dp[i][j] = [x for x in dp[i][j - 1] if x not in dp[i ^ (1 << j)][j - 1]]

winning_teams = []
for i in range(1 << n):
    winning_teams.extend(dp[i][-1])

print(*sorted(winning_teams), sep='\n')
