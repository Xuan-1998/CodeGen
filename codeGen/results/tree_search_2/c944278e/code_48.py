from itertools import combinations

def winning_teams(n, phases):
    # Initialize the state with all teams being winners initially
    state = [True] * (1 << n)
    
    for phase in phases:
        next_state = [False] * (1 << n)
        
        for team in range(1 << n):
            for i, bit in enumerate(bin(team)[2:].zfill(n)):
                if int(bit) ^ int(phase[i]):
                    # If the current team loses this round, it's no longer a winner
                    next_state[team] = False
                    break
        
        state = next_state
    
    return [i for i, win in enumerate(state) if win]

n = int(input())
phases = [int(x) for x in input().split()]

print(*winning_teams(n, phases), sep='\n')
