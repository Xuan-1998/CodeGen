python
# Step 1: Define the variables and read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Step 2: Calculate the total number of basketball players in the university
total_players = sum(s)

# Step 3: Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)
else:
    # Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 0
    for i in range(1, m):
        if h != i:
            prob += (s[h] + s[i]) / total_players
    print(prob)
