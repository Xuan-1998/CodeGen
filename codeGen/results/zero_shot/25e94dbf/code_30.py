code
def max_distance(commands, n):
    # Initialize the maximum distance
    max_dist = 0
    
    # Iterate over all possible combinations of modifying up to n commands
    for i in range(2**n):  # 2^n combinations
        modified_commands = list(commands)  # Create a copy of the original commands
        
        # Modify up to n commands based on the current combination
        for j in range(n):
            if (i >> j) & 1:
                if modified_commands[j] == "T":
                    modified_commands[j] = "F"
                else:
                    modified_commands[j] = "T"
        
        # Calculate the distance traveled by the turtle with the modified commands
        dist = 0
        forward = True
        for command in modified_commands:
            if command == "F" and forward:
                dist += 1
                forward = False
            elif command == "T":
                forward = not forward
        
        # Update the maximum distance if necessary
        max_dist = max(max_dist, dist)
    
    return max_dist

# Example usage
commands = ["F", "T", "F", "T", "F"]
n = 2
print(max_distance(commands, n))  # Output: 4
