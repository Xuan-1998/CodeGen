import sys
from math import comb

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of players
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
    exit()

# Calculate the number of players from the department of interest
players_from_department_interest = s[h-1]

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = 0.0

for i in range(players_from_department_interest + 1):
    probability += comb(players_from_department_interest, i) * (total_players - players_from_department_interest) ** (n-i-1) / comb(total_players, n)

print(probability)
