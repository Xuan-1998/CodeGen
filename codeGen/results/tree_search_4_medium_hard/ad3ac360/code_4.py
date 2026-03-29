def minCuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Initialize dp[0][n-1] to True
    dp[0][n-1] = True

    # Fill up the dp table using the transition relationship
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if (s[i] == s[j]) and ((i - 1 >= 0) and dp[i-1][j-1]) or (j + 1 < n) and dp[i+1][j+1]):
                dp[i][j] = True

    # Find the maximum i such that dp[i][n-1] is False
    cuts = 0
    for i in range(n):
        if not dp[i][n-1]:
            cuts += 1
        else:
            break

    return cuts


# Read input from stdin
s = input()

# Print the output to stdout
print(minCuts(s))
