# Step 1: Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Step 2: Calculate the total number of basketball players in the university
total_players = sum(s)

# Step 3: Check if there are enough players to form a team
if n > total_players:
    print(-1)
    exit()

# Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = (sum(s[:h]) + min(0, sum(s[h:]) - n + 1)) / total_players

print(probability)
