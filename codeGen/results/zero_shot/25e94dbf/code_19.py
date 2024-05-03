import sys

def max_distance(commands, n):
    # Initialize the distance traveled
    distance = 0
    
    # Initialize the number of turns remaining
    turns_left = n
    
    # Simulate the turtle's movement
    for command in commands:
        if command == "F":
            distance += 1
        elif command == "T" and turns_left > 0:
            distance = 0
            turns_left -= 1
    
    return distance

# Read the input from stdin
commands = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

# Calculate the maximum distance
max_dist = max_distance(commands, n)

# Print the answer to stdout
print(max_dist)
