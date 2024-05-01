from collections import defaultdict

def get_winners(n):
    # Initialize an empty set to store unique winning teams
    winners = set()
    
    def dfs(i, s):
        nonlocal winners
        
        if i == n:
            return
        for j in range(2**i):
            next_s = bin((int(s, 2) + (j << i)) % (2**n))[2:].zfill(n)
            
            # If the current team wins, add it to the set of winners
            if all(int(next_s[i-1-j], 2) > int(next_s[j], 2) for j in range(i)):
                winners.add(next_s)
                
            dfs(i+1, next_s)
    
    dfs(0, '0'*n)
    
    return sorted(list(winners))

# Read the input from stdin
n = int(input())
s = input()

print(get_winners(n))
