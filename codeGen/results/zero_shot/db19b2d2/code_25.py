# Step 1: Read input
n, m, h = map(int, input().split())  # number of players, departments, and department of interest
s = list(map(int, input().split()))  # number of basketball players in each department

# Step 2: Calculate the total number of basketball players
total_players = sum(s)

# Step 3: Check if there are enough players to form a team
if total_players < n:
    print(-1)  # output -1 if not enough players
else:
    # Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = sum(min(s[h-1], n) for s in s) / total_players
    
    # Step 5: Print the result
    print(probability)
