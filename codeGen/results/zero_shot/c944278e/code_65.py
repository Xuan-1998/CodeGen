n = int(input())
s = input()
winning_teams = []

for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if ((i >> j) & 1) == (int(s[j])):
            team_skill += 2**(n-j-1)
    winning_teams.append(team_skill)

print(*sorted(set(winning_teams)), sep='\n')
