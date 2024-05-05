import sys

# Read input
n, m, h = map(int, sys.stdin.readline().split())
players_in_departments = list(map(int, sys.stdin.readline().split()))

# Calculate total number of possible teams
total_teams = 1
for i in range(1, n+1):
    total_teams *= (m + i - 1) // i

# Count the number of possible teams that have at least one player from department of interest
teams_with_interest_player = sum(1 for _ in itertools.combinations(range(m), h))

pmf = teams_with_interest_player / total_teams

# Subtract PMF from 1 to get our desired probability
probability = 1 - pmf

print(probability)
