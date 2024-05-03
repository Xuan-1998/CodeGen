def max_distance(commands, n):
    # Initialize a dictionary to store the maximum distance for each command sequence
    dp = {"" : 0}

    # Iterate over each character in the commands string
    for i, command in enumerate(commands):
        new_commands = ""
        
        # Add all previous commands to the new_commands string
        for j in range(i+1):
            new_commands += commands[j]

        # Update the maximum distance based on the current command
        if command == "F":
            dp[new_commands] = max(dp.get(new_commands, 0), dp.get(new_commands+"T", 0) + i+1)
        else:
            dp[new_commands] = max(dp.get(new_commands, 0), dp.get(new_commands+"F", 0))

    # Return the maximum distance
    return dp[max(dp.keys())]

# Test the function
commands = input()
n = int(input())
print(max_distance(commands, n))
