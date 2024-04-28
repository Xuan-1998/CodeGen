n = int(input())
s = input()
winning_teams = []

for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if ((i >> j) & 1) == (int(s[n-1-j], 2) % 2):
            team_skill += 1
    winning_teams.append(team_skill)

winning_teams.sort()

print(*winning_teams, sep='\n')
