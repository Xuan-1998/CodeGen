import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = set()
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if ((i >> j) & 1):
            team_skill += int(s[j])
        else:
            team_skill -= int(s[j])
    winning_teams.add(team_skill)
winning_teams = sorted(list(winning_teams))
print(*winning_teams, sep='\n')
