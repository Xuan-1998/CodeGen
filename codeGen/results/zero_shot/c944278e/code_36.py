import sys
n = int(sys.stdin.readline())
s = str(sys.stdin.readline().strip())

winning_teams = []
for i in range(2**n):
    team_skill_level = 0
    for j in range(n):
        if ((i >> j) & 1) == 1:
            team_skill_level += int(s[j])
    winning_teams.append(team_skill_level)

winning_teams.sort()

print(*winning_teams, sep='\n')
