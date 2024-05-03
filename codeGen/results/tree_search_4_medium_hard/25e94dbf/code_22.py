def max_distance(commands, n):
    # Initialize the DP table
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0:
            dp[i] = 0
        elif i % 2 == 0:
            # If we're at an even index, consider two cases: 
            # either the previous command is 'T' or not.
            dp[i] = max(dp[i-1], commands[0] if i > 0 else 0)
        else:
            # If we're at an odd index, consider three cases: 
            # either the previous command is 'T', 'F', or neither (i.e., the first command).
            dp[i] = max(dp[i-1], commands[0] if i > 0 and n >= i else 0)

    return dp[-1]

# Read input
commands = list(input())
n = int(input())

print(max_distance(commands, n))
