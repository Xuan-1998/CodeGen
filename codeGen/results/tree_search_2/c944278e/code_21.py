import sys
from math import comb

def winning_teams(n, s):
    # Initialize the result list
    res = []
    
    # Calculate the number of phases
    k = len(s)
    
    # Generate all permutations of team indices
    for p in range(comb(2 ** n, k)):
        teams = [i for i in range(2 ** n) if ((p >> i) & 1)]
        
        # Check if this permutation is a winning team
        if s[0] == '1':
            res.append(teams)
        else:
            win = False
            for i in range(k):
                if (s[i] == '1' and sum((x >> i) & 1 for x in teams) > 0) or (s[i] == '0' and sum((x >> i) & 1 for x in teams) == 0):
                    win = True
                    break
            if win:
                res.append(teams)
    
    # Sort the result list
    res.sort()
    
    return '\n'.join(map(str, res))

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

print(winning_teams(n, s))
