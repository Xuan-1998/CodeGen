from collections import defaultdict

def find_winning_teams():
    n = int(input())
    s = input()
    
    dp = defaultdict(set)
    dp[0] = {0}  # Base case: only one team has won so far
    
    for i in range(1, 2**n):
        state = bin(i)[2:].zfill(n)  # Convert integer to binary string
        if s == state:
            teams = dp[i-1].copy()  # Get the winning teams from the previous phase
            for j in range(n):
                if state[j] == '0':
                    teams.add(2**j)
            dp[i] = teams
        else:
            dp[i] = set()
    
    winning_teams = set()
    for i in range(2**n-1, -1, -1):  # Iterate over the phases in reverse order
        if dp[i]:
            winning_teams.update(dp[i])
            break
    
    print(' '.join(map(str, sorted(winning_teams))))

if __name__ == "__main__":
    find_winning_teams()
