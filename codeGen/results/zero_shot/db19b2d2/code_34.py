import sys
def basketball_prob():
    # Read input
    n, m, h = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    
    # Calculate total number of players
    total_players = sum(s)
    
    # Check if there are enough players to form a team
    if total_players < n:
        return -1
    
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    prob = 0.0
    for i in range(m):
        if i == h-1:  # If we're considering the department of interest, add its size to our total players
            prob += s[i] / total_players * (1 - (s[i] / total_players) ** n)
        else:
            prob += s[i] / total_players * (1 - (s[i] / total_players) ** n) * (total_players - s[i]) / (total_players - 1)
    
    return prob
