from sys import stdin
from math import inf

def find_winning_teams(n):
    # Initialize a dictionary to store the results of subproblems
    memo = {}
    
    def dp(i, wins):
        if (i, wins) in memo:
            return memo[(i, wins)]
        
        if i == 0:
            return [wins]
        
        result = []
        for j in range(2**n):
            if bin(j)[2:].zfill(n)[i-1] == '1':
                # If the team has won its previous games
                winning_teams = dp(i-1, wins+1)
                for team in winning_teams:
                    result.append((team, 1))
            else:
                # If the team has lost its previous games
                losing_teams = dp(i-1, wins)
                for team in losing_teams:
                    result.append((team, -1))
        
        memo[(i, wins)] = sorted(result)
        return memo[(i, wins)]
    
    n = int(stdin.readline())
    winning_teams = dp(n, 0)
    print('\n'.join(map(str, [team[0] for team in winning_teams])))
