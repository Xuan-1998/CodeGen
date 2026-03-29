import sys
from functools import lru_cache

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of basketball players in all departments
total_players = sum(s)

# Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)  # Output -1 if not enough players
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = (sum(s[:h]) + s[h-1]) / total_players

    # Print the result to stdout
    print(prob)
