import sys
from math import comb

n, m, h = map(int, input().split())  # Read the number of players on a basketball team, the number of departments in a university, and the department of interest from stdin.
s = list(map(int, input().split()))  # Read the number of basketball players in each department from stdin.

# Calculate the total number of players
total_players = sum(s)

# If there are not enough basketball players to form a team, output -1 instead
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest.
    probability = 1 - sum(comb(s[i], h, exact=True) / comb(total_players, h, exact=True) for i in range(m)) if total_players >= n else 0
    print(probability)
