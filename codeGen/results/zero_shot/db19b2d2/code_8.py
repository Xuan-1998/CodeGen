import sys
from math import comb

# Read inputs from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of possible teams
total_teams = comb(sum(s), n)

# Calculate the number of teams that don't have any player from the department of interest
teams_without_h = 1
for i in range(m):
    if i != h:
        teams_without_h *= comb(sum([s[j] for j in range(m) if j != i]), n)
    else:
        teams_without_h *= 1

# Calculate the probability
probability = teams_without_h / total_teams if total_teams > 0 else -1

# Print the answer to stdout
print(probability)
