import sys

def max_distance(commands, n):
    # Initialize the maximum distance
    max_dist = 0
    
    # Loop through each command
    for i in range(len(commands)):
        # If it's a turn around, update the direction
        if commands[i] == "T":
            if i < n:
                # Modify the command to move forward instead
                commands[i] = "F"
        # If it's a movement, update the distance
        elif commands[i] == "F":
            max_dist += 1
    
    return max_dist

# Read input from stdin
commands = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

# Calculate and print the maximum distance
print(max_distance(commands, n))
