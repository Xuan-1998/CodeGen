# Read the input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate the total number of basketball players
total_players = sum(s)

# Check if there are not enough basketball players in the university to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 1 - (n-1) / (total_players - s[h-1])
    
    # Print the answer
    print(probability)
