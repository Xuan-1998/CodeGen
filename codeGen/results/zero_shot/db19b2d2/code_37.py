import sys
from math import comb

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the number of basketball players available in total
total_players = sum(s)

# Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the number of basketball players not from the department of interest
    non_h_players = sum(s[:h-1]) + sum(s[h:])

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1 - comb(non_h_players, n) / comb(total_players, n)

    print(prob)
