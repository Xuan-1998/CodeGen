import sys
from math import comb

# Read the input values
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of players available
total_players = sum(s)

# If there are not enough basketball players in the university to form a team, output -1 instead
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 0.0
    for i in range(h):
        if s[i] >= n:
            prob = 1.0
            break
        else:
            prob += comb(s[i], n) / (comb(total_players, n))
    
    # Print the result with a precision of 10^-6
    print(format(prob, '.6f'))
