def solve(n, s):
    # Create a dynamic programming table with size 2^n x n
    dp = [[set() for _ in range(1 << n)] for _ in range(n + 1)]
    
    # Fill up the dynamic programming table using nested loops
    for i in range(n):
        for j in range(1 << i, 1 << (i + 1)):
            if s[i] == '1':
                # If the current team wins, add it to the set of winning teams
                dp[i + 1][j].add(j)
            else:
                # If the current team loses, combine the sets of winning teams
                for k in range(1 << i):
                    if k & j:  # Check if there are any winning teams in the previous phase
                        dp[i + 1][j].update(dp[i][k])
    
    # Find the winning teams by checking if any team has won at least one game in each phase
    winning_teams = set()
    for i in range(n, -1, -1):
        for j in range(1 << i, 1 << (i + 1)):
            if dp[i][j]:
                winning_teams.update(dp[i][j])
    
    # Sort the set of winning teams in ascending order
    winning_teams = sorted(list(winning_teams))
    
    return ' '.join(map(str, winning_teams))

n = int(input())
s = input()
print(solve(n, s))
