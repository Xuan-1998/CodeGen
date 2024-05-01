import sys
from itertools import product

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = set()
for team in product('01', repeat=n):
    # Check if the team can win
    team_can_win = True
    for i, result in enumerate(s):
        if (result == '1' and sum(int(b) for b in team[:i+1]) % 2 == 0) or \
           (result == '0' and sum(int(b) for b in team[:i+1]) % 2 != 0):
            team_can_win = False
            break
    if team_can_win:
        winning_teams.add(''.join(team))

# Print the winning teams to stdout
print('\n'.join(sorted(winning_teams)))
