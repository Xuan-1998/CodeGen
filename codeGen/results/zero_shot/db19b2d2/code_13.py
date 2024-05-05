def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    # Calculate the total number of players
    total_players = sum(s)
    
    # Check if there are not enough basketball players in the university to form a team
    if total_players < n:
        return -1
    
    # Initialize the probability that a randomly formed team will have at least one player from the department of interest
    prob = 0
    
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    for i in range(m):
        if i == h:
            continue
        prob += (s[i] / total_players) * (1 - sum(s[j] / total_players for j in range(i)) ** n)
    
    # Return the probability that a randomly formed team will have at least one player from the department of interest
    return prob

if __name__ == "__main__":
    print(solve())
