import sys

# Read input
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate total number of players in the university
total_players = sum(s)

# Calculate probability that a randomly formed team will have at least one player from the department of interest
probability = (total_players - sum(sj for j in range(m) if j != h)) / total_players if total_players >= n else -1

print(probability)
