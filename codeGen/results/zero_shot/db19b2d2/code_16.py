import sys
from functools import lru_cache

# Read input from stdin
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Calculate total number of basketball players in university
total_players = sum(s)

# If there are not enough basketball players to form a team, return -1
if total_players < n:
    print(-1)
else:
    # Calculate the number of departments that can contribute at least one player
    @lru_cache(None)
    def count_depts(candidates):
        if candidates < 0 or sum(1 for i in range(h-1) if s[i] > 0) == 0:
            return 0
        else:
            return sum(count_depts(candidates - 1) for _ in range(s[h-1]))

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = count_depts(total_players - 1) / total_players

    # Print the result to stdout
    print(prob)
