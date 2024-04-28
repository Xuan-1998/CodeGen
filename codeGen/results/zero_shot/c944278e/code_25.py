n = int(input())
s = input()
winning_teams = []
for i in range(2**n):
    team_skill = [0] * n
    skill_level = 0
    for j in range(n):
        if (i >> j) & 1:
            team_skill[j] += 1
            skill_level += int(s[j], 2)
    winning_teams.append((skill_level, i))
winning_teams.sort(reverse=True)
for team in winning_teams:
    print(team[1])
