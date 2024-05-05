import sys
from math import comb, factorial

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
h = int(sys.stdin.readline().strip())

players_per_department = list(map(int, sys.stdin.readline().split()))

total_players = sum(players_per_department)
players_from_h = players_per_department[h-1]

team_size = min(n, total_players)

# Calculate the probability that a team will have at least one player from department h
probability = 0

for i in range(team_size + 1):
    if i > 0:
        probability += comb(total_players - 1, i - 1) / factorial(total_players)
    else:
        probability -= comb(total_players, i) / factorial(total_players)

# Calculate the probability that a team will have at most zero players from department h
probability_from_zero = sum(comb(players_per_department[i-1], j) for i in range(1, m+1) for j in range(n+1))

probability *= 1 - probability_from_zero

print(probability)
