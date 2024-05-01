import sys

def generate_teams(n):
    teams = []
    for i in range(2**n):
        team = [int(c) for c in bin(i)[2:].zfill(n)]
        teams.append(team)
    return teams

def is_winning_team(team, n):
    wins = 0
    for match in team:
        if match == 1:
            wins += 1
    return wins == n

n = int(sys.stdin.readline())
teams = generate_teams(n)

winning_teams = []
for team in teams:
    if is_winning_team(team, n):
        winning_teams.append(team)

print(*sorted(winning_teams), sep='\n')
