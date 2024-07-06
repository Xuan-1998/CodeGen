import sys

n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of basketball players in the university
total_players = sum(s)

# Check if there are enough basketball players to form a team
if n > total_players:
    print(-1)
    exit()

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = 1 - (sum([min(n, s[i]) for i in range(m) if i != h]) / total_players)**n

print(probability)
