# Read input
n, m, h = map(int, input().split())
dept_players = list(map(int, input().split()))

# Calculate the total number of basketball players
total_players = sum(dept_players)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1 - (sum(min(n, dept_players[i]) for i in range(m)) / total_players) ** n
    
    # Print the result
    print(prob)
