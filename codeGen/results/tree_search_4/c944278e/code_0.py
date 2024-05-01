import sys

def find_winning_teams(n, s):
    dp = [[False] * (1 << n) for _ in range(n + 1)]

    # Initialize dp[0][j] = (s[0] == '1') for all j
    for j in range(1 << n):
        dp[0][j] = (s[0] == '1')

    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(1 << i):
            if s[i - 1] == '1':
                for k in range(1 << (i - 1)):
                    if dp[i - 1][k]:
                        dp[i][j] = True
                        break

    # Find all winning teams and print them
    for i in range(n + 1):
        for j in range(1 << i):
            if dp[i][j]:
                print(j, end=' ')
        print()

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# Solve the problem and print the answer
find_winning_teams(n, s)
