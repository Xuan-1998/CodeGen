import math

def calculate_probability():
    # Read input from stdin
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    # Calculate the total number of basketball players
    total_players = sum(s)

    # Check if there are not enough basketball players in the university to form a team
    if total_players < n:
        print(-1)
        return

    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    probability = 0
    for i in range(1, m):
        probability += math.comb(s[i], n - 1) / math.comb(total_players, n - 1)
    
    print(probability)

calculate_probability()
