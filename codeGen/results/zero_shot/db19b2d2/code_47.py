import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    # Calculate the total number of basketball players
    total_players = sum(s)

    # Check if there are enough players to form a team
    if total_players < n:
        return -1

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 0
    for i in range(1, m+1):
        if i == h:  # If we're interested in this department
            continue
        comb_players = total_players - sum(s[:i-1]) - sum(s[i:])
        prob += (comb(n, min(comb_players, n)) * s[h-1] / comb(total_players, n))
    return prob

print(solve())
