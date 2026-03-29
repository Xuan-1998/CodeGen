import sys
from math import comb

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of players in all departments
total_players = sum(s)

# Check if there are enough players to form a team
if n > total_players:
    print(-1)
    sys.exit()

# Calculate the probability that a randomly formed team will have at least one player from the department of interest
probability = 0
for i in range(1, m+1):
    department_players = sum(1 for j in s if j >= i and j > 0)
    total_combinations = comb(total_players, n)
    department_combinations = comb(department_players, n)
    probability += (department_combinations / total_combinations)

print(probability)
