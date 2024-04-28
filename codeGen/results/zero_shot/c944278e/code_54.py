import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
winning_teams = []
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if (i >> j) & 1:
            team_skill += int(s[n-1-j])
        else:
            team_skill -= int(s[n-1-j])
    winning_teams.append(team_skill)
winning_teams.sort()
print('\n'.join(map(str, [str(i) for i in winning_teams])))
