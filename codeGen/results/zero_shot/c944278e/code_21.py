n = int(input())
s = input()
teams = [i for i in range(2**n)]
winning_teams = []

for i in range(n):
    teams = [(team >> (1 << i)) & 1 if bit == '0' else team for team, bit in zip(teams, s[i:][::-1])]

for team in teams:
    if all((team >> (1 << i)) & 1 > 0 if bit == '0' else (team >> (1 << i)) & 1 < 1 for i, bit in enumerate(reversed(s))):
        winning_teams.append(team)

print(*sorted(winning_teams), sep='\n')
