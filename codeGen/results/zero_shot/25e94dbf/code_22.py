import sys

def max_distance(commands, n):
    max_distance = 0
    current_direction = 0

    for command in commands:
        if command == "F":
            max_distance += 1
        elif command == "T" and n > 0:
            # Modify the command to move forward or turn around
            if current_direction == 0:  # Move forward
                command = "F"
                current_direction = 1  # Turn around
            else:  # Turn around
                command = "T"
                current_direction = 0  # Move forward
            n -= 1

    return max_distance

# Read input from stdin
commands = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

# Calculate the maximum possible distance
max_distance = max_distance(commands, n)

# Print the answer to stdout
print(max_distance)
