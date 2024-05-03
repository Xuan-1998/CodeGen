def max_turtle_distance(commands, n):
    # Initialize dp array to store maximum distances for each subproblem
    dp = [0] * (len(commands) + 1)
    
    for i in range(1, len(commands) + 1):
        if commands[i - 1] == "T":
            # If the current command is "T", we can either turn around and move back
            # or continue moving forward. We take the maximum of these two options.
            dp[i] = max(dp[i - 1], dp[i - 2] - 1)
        else:
            # If the current command is "F", we can either move forward one step
            # or turn around and move back to a previous position. We take the maximum of these two options.
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
    
    # Return the maximum distance traveled, considering all modifications (n)
    return dp[-1]

# Test the function
commands = input()  # Read the commands from stdin
n = int(input())  # Read n from stdin

print(max_turtle_distance(commands, n))  # Print the result to stdout
