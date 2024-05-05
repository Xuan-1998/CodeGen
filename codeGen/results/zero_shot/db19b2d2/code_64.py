import math

# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of basketball players in all departments
total_players = sum(s)

# Check if there are not enough basketball players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1 - math.pow(1 - (s[h-1] / total_players), n)
    print(prob)
