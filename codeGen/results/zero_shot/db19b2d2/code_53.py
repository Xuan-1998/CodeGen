# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of players in all departments
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 1 - (total_players - sum(s[h-1:])) / (n * total_players) if h else 0.5
    
    # Print the result to stdout
    print(prob)
