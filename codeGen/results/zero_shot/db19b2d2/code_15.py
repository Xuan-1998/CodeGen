# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of players
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    num_departments_with_players = s.count(0) - 1
    prob = (m - h - num_departments_with_players) / m
    if n > total_players - sum(range(h+1)):
        prob = 1
    print(prob)
