def minCuts(s):
    n = len(s)
    # Create a table to store whether each substring is a palindrome or not
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    # Initialize the count of cuts to 0
    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1
    return cuts


# Read input from stdin
s = input()

# Print the output to stdout
print(minCuts(s))
