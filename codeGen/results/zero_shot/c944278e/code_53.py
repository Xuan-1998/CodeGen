n = int(input())
s = input()

winning_teams = []

for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if ((i >> j) & 1) and s[j] == '1':
            team_skill += 1
        elif not ((i >> j) & 1) and s[j] == '0':
            team_skill -= 1
    if team_skill > 0:
        winning_teams.append(i)

winning_teams.sort()
print(*winning_teams, sep='\n')
