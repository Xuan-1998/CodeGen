# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Sort the number of players in each department
s.sort()

# Calculate the total number of basketball players
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 0
    for i in range(h-1, m):
        probability += s[i] - (s[h-1] if i == h-1 else 0)
    
    print(probability / total_players)
