# Read the input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of basketball players
total_players = sum(s)

# Calculate the minimum number of players needed from the department of interest
min_players_from_h = max(0, min(n, s[h]))

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = (s[h] / total_players) ** min_players_from_h

print(probability)
