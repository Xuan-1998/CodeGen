n = int(input())
s = input()
teams = 2**n
winning_teams = []
for i in range(1, teams+1):
    team = bin(i)[2:].zfill(n)
    if all(int(a) <= int(b) for a, b in zip(s, team)):
        winning_teams.append(team)

print(*sorted(winning_teams), sep='\n')
