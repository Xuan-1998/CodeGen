code
import sys

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
players_per_department = list(map(int, sys.stdin.readline().split()))

# Check if there are enough basketball players in the university to form a team
if sum(players_per_department) < n:
    print(-1)
    sys.exit()

# Calculate the total number of players available from the department of interest
total_players_from_interest = players_per_department[h-1]

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = 1 - (sum(players_per_department[:h-1]) + sum(players_per_department[h:])) / n

print(probability)
