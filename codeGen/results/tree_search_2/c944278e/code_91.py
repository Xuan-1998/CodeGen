from collections import defaultdict

def winning_teams(n, s):
    dp = [0] * (1 << n)  # Initialize dp array with zeros
    teams = list(range(2 ** n))  # Generate all team IDs
    
    for i in range(2 ** n):  # Iterate over each team ID
        state = 0  # Initialize current state
        
        for j in range(n):
            if ((i >> j) & 1):  # If bit j is set in the team ID
                state ^= (1 << s[j])  # XOR with the corresponding skill level
        
        dp[i] = state  # Update the dp array with the current state
        
    winners = []  # Initialize list of winning teams
    
    for i in range(2 ** n):  # Iterate over each team ID
        if dp[i] == 0:  # If the current team can win
            winners.append(i)  # Add the team ID to the list of winners
    
    return sorted(winners)
