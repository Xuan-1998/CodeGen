def winning_teams(n, s):
    # Initialize a 2D array to store the memoized results
    dp = [[False] * (1 << n) for _ in range(n + 1)]

    # Base case: When s = '1'*n, only one team can win (the first one)
    dp[0][1] = True

    for i in range(1, n + 1):
        for j in range((1 << i) - 1, -1, -1):  # Iterate from right to left
            if not dp[i - 1][j]:  # If the current team doesn't win
                continue

            # Calculate the score of the next phase (bitwise OR)
            j_new = j | (1 << i)

            # Check if the new score is a winning condition
            if (s[i - 1] == '1' and not dp[i][j_new]) or (s[i - 1] == '0' and dp[i][j]):
                dp[i][j_new] = True

    # Find all winning teams and print them in ascending order
    winning_teams = []
    for j in range((1 << n) - 1, -1, -1):
        if dp[n][j]:
            winning_teams.append(j)

    return sorted(winning_teams)
