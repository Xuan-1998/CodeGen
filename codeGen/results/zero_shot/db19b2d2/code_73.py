# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of basketball players
total_players = sum(s)

# Calculate the minimum required players from the department of interest
required_players = max(0, s[h-1])

# If there are not enough basketball players in the university to form a team, output -1
if total_players < n:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 1 - (total_players - required_players) / total_players ** (n-1)
    print(probability)
