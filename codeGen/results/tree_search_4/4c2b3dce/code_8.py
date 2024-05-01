def is_valid(s):
    n = len(s)
    dp = [False] * (n + 1)  # Initialize DP table

    for i in range(n):
        if s[i:i+2] == "AB" or s[i:i+2] == "BA":
            if i >= 2 and s[i-2:i] == "BA" or s[i-2:i] == "AB":
                dp[i + 1] = True
            else:
                dp[i + 1] = False

    return dp[-1]

# Read input from stdin
s = input()

# Print the result to stdout
print("YES" if is_valid(s) else "NO")
