def calculate_probability():
    n, m, h = map(int, input().split())  # read input
    s = list(map(int, input().split()))  # read input
    
    total_players = sum(s)
    
    if total_players < n:  # not enough players to form a team
        return -1.0
    
    players_from_interest_dept = s[h-1]  # number of players from the department of interest
    
    probability = (players_from_interest_dept / total_players) ** n  # calculate the probability
    
    return 1.0 - probability  # subtract from 1 to get the probability that a randomly formed team will have at least one player from the department of interest
