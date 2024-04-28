n = int(input())
s = input()

winning_teams = []
for i in range(2**n):
    team = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            team[j] = 1
    if all(s[k] == str(int(team[k])) for k in range(n)):
        winning_teams.append(i)

winning_teams.sort()
print(*winning_teams, sep='\n')
