import sys

def find_winning_teams(n, s):
    # Initialize dp array with zeros
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    # Base case: only one team remains at the end of the tournament
    for j in range(1 << n):
        if bin(j).count('1') == 1:
            dp[n][j] = 1

    # Fill up the dp array using dynamic programming
    for i in range(n - 1, -1, -1):
        for j in range(1 << n):
            if s[i] == '0':
                dp[i][j] = max(dp[i][j], dp[i + 1][j])
            else:
                for k in range(j):
                    if (k & ~j) >> i == s[i]:
                        dp[i][j] = max(dp[i][j], dp[i + 1][k] + 1)

    # Return all indices j such that dp[n][j] > 0
    return [j for j in range(1 << n) if dp[n][j] > 0]

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# Print the result to stdout
print(*find_winning_teams(n, s), sep='\n')
