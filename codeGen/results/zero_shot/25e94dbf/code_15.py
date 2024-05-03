def max_distance(commands, n):
    # Initialize variables
    total_distance = 0
    turns = 0
    
    # Iterate over each command
    for i in range(len(commands)):
        if commands[i] == "F":
            # Move forward and count the distance traveled
            total_distance += 1
        elif commands[i] == "T":
            # Turn around, but don't move backward yet
            turns += 1
    
    # Modify up to n commands
    for _ in range(min(n, turns)):
        # Replace a turn command with a forward movement
        if commands[turns-1] == "T":
            commands[turns-1] = "F"
    
    # Count the total distance traveled after modifications
    total_distance += sum(1 for c in commands if c == "F")
    
    return total_distance

# Test the function
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
