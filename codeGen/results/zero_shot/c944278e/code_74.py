import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

teams = [i for i in range(2**n)]
winning_teams = []

for i in range(n):
    bit = (1 << i)
    losing_teams = []
    winning_teams_temp = []
    
    for team in teams:
        if ((team >> i) & 1) == int(s[i]):
            losing_teams.append(team)
        else:
            winning_teams_temp.append(team)
    
    teams = losing_teams
    winning_teams.extend(winning_teams_temp)

winning_teams.sort()
print(' '.join(map(str, winning_teams)))
