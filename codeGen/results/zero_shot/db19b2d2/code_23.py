import sys

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
dept_sizes = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of basketball players in the university
total_players = sum(dept_sizes)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    dept_size_h = dept_sizes[h-1]
    prob = 1 - (n-1) / total_players ** n
    print(prob)
