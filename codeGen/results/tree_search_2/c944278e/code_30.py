def findWinningTeams(n, s):
    # Initialize the dynamic programming table with zeros
    dp = [[0]*2 for _ in range(n+1)]

    # Fill the base case: a team with no wins has skill level 0
    for i in range(2**n):
        mask = (i << (n-1))
        j = n - 1
        while j >= 0:
            if ((mask >> j) & 1):
                dp[j][0] += 1
            else:
                dp[j][1] += 1
            j -= 1

    # Fill the table using dynamic programming
    for i in range(n-1, -1, -1):
        for j in range(2):
            if s[i] == '1':
                dp[i][j] = max(dp[i+1][0], dp[i+1][1])
            else:
                if j == 0:
                    dp[i][j] = dp[i+1][0]
                else:
                    dp[i][j] = dp[i+1][1]

    # Find the winning teams
    winning_teams = set()
    for i in range(2**n):
        mask = (i << (n-1))
        j = n - 1
        while j >= 0:
            if ((mask >> j) & 1):
                if dp[j][0] > dp[j][1]:
                    winning_teams.add(i)
            else:
                if dp[j][1] > dp[j][0]:
                    winning_teams.add(i)
            j -= 1

    # Sort the winning teams and print them
    for team in sorted(list(winning_teams)):
        print(bin(team)[2:].zfill(n))

# Example usage
n = int(input())
s = input()
findWinningTeams(n, s)
