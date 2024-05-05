# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Sort departments by number of players in descending order
s.sort(reverse=True)

# Calculate total number of players
total_players = sum(s)

# Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate probability
    probability = 0
    for i, count in enumerate(s):
        if i == h:  # department of interest
            probability += (n - sum(s[:i])) * (count / total_players) ** n
        else:
            probability -= (sum(s[:i]) + count) * (1 - (count / total_players)) ** n

    print(probability)
