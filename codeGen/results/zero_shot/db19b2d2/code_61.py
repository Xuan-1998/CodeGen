import math

def calculate_probability():
    # Read input
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    # Calculate total number of possible teams without players from department of interest
    total_teams_without_interest = 1
    for i in range(m):
        if i != h:
            total_teams_without_interest *= math.comb(n - s[i], n)

    # Calculate probability
    if total_teams_without_interest == 0:
        return -1
    else:
        return 1 - total_teams_without_interest / math.comb(n, n)

print(calculate_probability())
