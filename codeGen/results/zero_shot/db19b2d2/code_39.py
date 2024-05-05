import sys

# Read input values
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

total_players = sum(s)
if total_players < n or n > 100:  # check if there are enough players and if n is within the constraint
    print(-1)
else:
    # Calculate the number of ways to form a team without any player from department h
    no_h_players = sum(min(n, si) for si in s[:h-1] + s[h+1:])
    no_teams = 2**n  # total number of possible teams

    # Calculate the probability
    probability = (no_teams - no_h_players) / no_teams

    print(probability)
