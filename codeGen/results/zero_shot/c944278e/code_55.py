import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = []
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if ((i >> j) & 1):
            team_skill += int(s[j])
    winning_teams.append(team_skill)
print(*sorted(set(winning_teams)), sep='\n')
