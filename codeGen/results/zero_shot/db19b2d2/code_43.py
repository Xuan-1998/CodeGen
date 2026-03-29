import sys
from math import comb

def calculate_probability(n, m, h, s):
    # Calculate the total number of players available
    total_players = sum(s)

    # If there are not enough basketball players in the university to form a team, output -1
    if total_players < n:
        return -1.0

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    # We need to subtract 1 from the number of departments and the department of interest because we're interested in having at least one player from this department, not exactly one
    probability = sum(comb(s[i], n-1) for i in range(h)) / comb(total_players, n)

    return round(probability, 6)
