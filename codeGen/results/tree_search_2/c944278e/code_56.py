def winning_teams(n):
    # Read input from stdin
    n = int(input())
    s = list(map(int, input().strip()))

    # Initialize 2D table for dynamic programming
    dp = [[0] * (1 << n) for _ in range(n)]

    # Base case: When n = 1, there's only one team that can win
    for i in range(2**n):
        dp[0][i] = sum((s[j] & 1) == 1 for j in range(n)) + (i >= 2**n//2)

    # Dynamic programming iteration
    for i in range(1, n):
        for j in range(1 << (n - i)):
            dp[i][j | (1 << i)] = min(dp[i-1][k] for k in range(1 << (i-1))) + 1

    # Find winning teams
    winning_teams = []
    for i in range(2**n):
        if dp[n-1][i] == n:
            winning_teams.append(i)

    # Print the result to stdout
    print(*sorted(winning_teams), sep='\n')

# Call the function with the input values
winning_teams(n)
