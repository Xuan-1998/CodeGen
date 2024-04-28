n = int(input())
s = input()
winning_teams = []
for i in range(2**n):
    team_skill_level = 0
    for j in range(n):
        if (i & (1 << j)) != 0:
            team_skill_level += 1
    if sum([int(x) for x in s]) % 2 == team_skill_level % 2:
        winning_teams.append(i)
winning_teams.sort()
for team in winning_teams:
    print(team)
