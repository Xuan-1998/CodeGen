# Step 1: Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Step 2: Calculate the total number of players in the university
total_players = sum(s)

# Step 3: Check if there are enough players to form a team
if n > total_players:
    print(-1)  # If not, output -1

# Step 4: Calculate the probability that a randomly formed team will have at least one player from the department of interest
players_from_interest = s[h-1]
total_teams = total_players // n
prob_at_least_one = (total_players - players_from_interest) / total_players + (players_from_interest * total_teams) / total_players

print(prob_at_least_one)
