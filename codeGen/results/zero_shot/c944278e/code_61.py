n = int(input())
s = input()
winning_teams = []
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if (i >> j) & 1:
            team_skill += 1 << j
    if s != str(team_skill ^ int(s, 2)):
        winning_teams.append(i)
print(*sorted(winning_teams), sep='\n')
