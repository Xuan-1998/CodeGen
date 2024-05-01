import sys

def find_winning_teams(n, s):
    # Generate all possible teams
    teams = [i.toBinary() for i in range(2**n)]
    
    winning_teams = []
    
    for team in teams:
        path = ''
        for i in range(n):
            if (int(s[i]) ^ int(team[i])) == 1:
                path += '1'
            else:
                path += '0'
        
        # Check if the team's path ends with a win
        if path == '1' * n:
            winning_teams.append(team)
    
    return sorted(winning_teams)

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(*find_winning_teams(n, s), sep='\n')
