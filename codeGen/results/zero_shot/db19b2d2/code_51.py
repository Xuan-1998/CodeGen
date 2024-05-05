import sys
from math import comb

def calculate_probability(n, m, h, s):
    # Calculate the total number of basketball players
    total_players = sum(s)
    
    # Check if there are enough basketball players to form a team
    if total_players < n:
        return -1
    
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 0
    for i in range(h, m):
        probability += comb(s[i], n) / (comb(total_players, n))
    
    return probability

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate and print the probability
print(calculate_probability(n, m, h, s))
