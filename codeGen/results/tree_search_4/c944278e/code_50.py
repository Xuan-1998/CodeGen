import sys

n = int(input())
winning_teams = []
for i in range(2**n):
    team = bin(i)[2:].zfill(n)
    wins = sum(int(c) for c in team)
    if wins >= 1:
        winning_teams.append(team)

print(*sorted(winning_teams), sep='\n')
