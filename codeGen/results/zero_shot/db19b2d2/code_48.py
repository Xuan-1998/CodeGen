# Step 1: Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Step 2: Calculate the total number of basketball players
total_players = sum(s)

# Step 3: Calculate the minimum required number of players from the department of interest
required_players = max(0, s[h-1])

# Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = (sum(min(r, total_players-r) for r in range(required_players+1)) / total_players)

print(probability)
