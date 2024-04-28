def find_winning_teams(n):
    # Initialize a 2D table to store the winning teams for each round
    dp = [[[] for _ in range(1 << n)] for _ in range(n)]
    
    # Base case: Only one team wins when there's only one round
    for i in range(2**n):
        dp[0][i] = [str(i).zfill(n)]
    
    # Iterate through each round and consider all possible outcomes
    for i in range(1, n):
        for j in range(2**(n-i)):
            # Determine the winning teams for this round based on the previous round's outcome
            win_teams = dp[i-1][j][0]
            if (j >> (i-1)) & 1:
                # Team with higher skill level wins, so add it to the list of winners
                win_teams += [str((j | 2**(n-i)))].zfill(n)
            else:
                # Team with lower skill level wins, so add it to the list of winners
                win_teams = [str((j | 2**(n-i)))].zfill(n)
            
            # Update the table with the winning teams for this round
            dp[i][j] = sorted(set([team.split(' ')[0] for team in win_teams]))

    # Print out all the winning teams in ascending order
    for i in range(1 << n):
        if dp[-1][i]:
            print(' '.join(sorted(set(dp[-1][i]))))

if __name__ == "__main__":
    n = int(input())
    find_winning_teams(n)
