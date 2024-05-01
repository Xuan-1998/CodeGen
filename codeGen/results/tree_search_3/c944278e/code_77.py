def find_winning_teams():
    n = int(input())
    s = input()
    
    winning_teams = set()
    
    # Process all phases
    for i in range(n):
        phase_winner = '1' if s[i] == '1' else '0'
        
        # Update the set of winning teams based on the current phase's winner
        if phase_winner == '1':
            winning_teams.update({f"Team {2**i}"})
        else:
            for team in list(winning_teams):
                if int(team.split(' ')[1]) <= 2**i:
                    winning_teams.remove(team)
    
    # Sort the winning teams and print them
    print(*sorted(list(winning_teams)), sep='\n')

find_winning_teams()
