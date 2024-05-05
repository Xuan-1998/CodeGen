# Step 1: Read input
n, m, h = map(int, input().split())  # number of players, departments, and department of interest
s = list(map(int, input().split()))  # number of basketball players in each department

# Step 2: Calculate the total number of basketball players
total_players = sum(s)

# Step 3: Check if there are enough basketball players to form a team
if total_players < n:
    print(-1)
else:
    # Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
    players_from_interest = s[h-1]  # number of basketball players in the department of interest
    total_prob = (n - 1) / n  # probability that a randomly formed team does not include any players from the department of interest
    prob_interest = 1 - total_prob  # probability that a randomly formed team includes at least one player from the department of interest

    print(prob_interest)
