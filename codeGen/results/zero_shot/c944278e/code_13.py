n = int(input())
s = input()

winning_teams = []
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if (i & (1 << j)) != 0:
            team_skill += int(s[j])
    winning_teams.append((team_skill, i))

winning_teams.sort()

print(*[str(team) for team, _ in winning_teams], sep='\n')
