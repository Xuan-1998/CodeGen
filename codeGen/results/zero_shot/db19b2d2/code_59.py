def calculate_probability():
    # Read input
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    # Calculate total number of players
    total_players = sum(s)

    # Check if there are enough players to form a team
    if total_players < n:
        return -1

    # Calculate probability that at least one player from the department of interest is in the team
    probability = 1 - (total_players - s[h-1]) / (total_players * (n-1) + 1)

    return round(probability, 6)
