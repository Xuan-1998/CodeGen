# Step 1: Read the input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Step 2: Calculate the total number of players in the university
total_players = sum(s)

# Step 3: Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)  # If not, output -1

else:
    # Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = sum(min(n, si) for si in s[:h]) / total_players
    print(prob)
