import sys

# Read input
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate total number of players in all departments
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate probability that at least one player is from the department of interest
    probability = 1 - (sum(min(n, s[i]) for i in range(m) if i != h) + sum(0 for _ in range(h))) / total_players ** n

    # Print result
    print(probability)
