import math

# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate total number of players
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate probability that at least one player from the department of interest is selected
    probability = 1 - math.prod((1 - s[h] / total_players) ** (n-1))
    
    print(probability)
