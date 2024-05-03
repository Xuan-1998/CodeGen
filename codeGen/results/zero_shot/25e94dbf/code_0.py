import sys

# Read input from stdin
commands = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

# Initialize variables
max_distance = 0
current_direction = 1  # 1: forward, -1: backward
total_forward_moves = 0

for i in range(len(commands)):
    if commands[i] == 'F':
        total_forward_moves += 1
        max_distance += current_direction
    elif commands[i] == 'T' and n > 0:
        n -= 1
        # If we've used up all our modifications, turn around (reset direction)
        if n == 0:
            current_direction *= -1

# Print the maximum distance to stdout
print(max_distance)
