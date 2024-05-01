def find_winning_teams(n, s):
    # Initialize a list to store the permutations of winning teams
    winning_teams = []
    
    for i in range(2**n):
        permutation = [str((i >> j) & 1) for j in range(n)]
        phase_result = ''
        
        # Evaluate the results of each phase
        for k in range(n):
            if s[k] == '0':
                phase_result += '0'
            else:
                phase_result += str(int(permutation[n-1-k]) ^ int(s[n-1-k]))
                
        # Check if this permutation is a winning team
        if all(phase_result[i] == s[i] for i in range(n)):
            winning_teams.append((i, phase_result))
    
    # Sort the winning teams by their skill levels and return them
    winning_teams.sort(key=lambda x: int(''.join(map(str, list(x[1])))), reverse=True)
    return [team[0] for team in winning_teams]
