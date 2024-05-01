import sys

n = int(sys.stdin.readline())
winning_teams = set()

def transition_function(phase, teams):
    # Update the state based on the results of matches
    next_teams = set()
    for team in teams:
        # Check if this team has won or lost
        if (team >> phase) & 1:  # Team has won
            next_teams.add(team)
        else:  # Team has lost
            next_teams.update({t for t in teams if not ((t ^ team) & (1 << phase))})
    return next_teams

for _ in range(n):
    phase = int(sys.stdin.readline())
    teams = set()
    for i in range(2 ** n):  # Iterate through all possible teams
        if (i >> (n - 1)) & 1:  # Team has won the current phase
            teams.add(i)
        else:  # Team has lost the current phase
            teams.update({t for t in {0, 1} ** n if not ((t ^ i) & (1 << (n - 1)))})
    winning_teams = winning_teams.union(transition_function(phase, teams))

print('\n'.join(map(str, sorted(winning_teams))))
