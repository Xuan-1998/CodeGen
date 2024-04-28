import sys

def winners(n, s):
    dp = [[0] * (1 << n) for _ in range(n)]
    
    # Initialize base case: team with all wins has won the tournament
    for i in range(2 ** n):
        dp[0][i] = 1 if bin(i).count('1') > 2 ** (n - 1) else 0
    
    for i in range(n - 1):
        for j in range(2 ** n):
            # Calculate the number of wins for the current team
            wins = sum((s[k] >> i) & 1 for k in range(i + 1, n))
            
            # Update the dynamic programming table
            for m in range(2 ** (n - i - 1)):
                dp[i + 1][j | m] = max(dp[i + 1][j | m], dp[i][m] if wins > sum((s[k] >> i) & 1 for k in range(n - 1, i, -1)) else dp[i][m])
    
    # Return the winning teams
    return [i for i in range(2 ** n) if dp[n - 1][i]]

# Read input from stdin
n = int(input())
s = list(map(int, input().split()))

print(*winners(n, s), sep='\n')
