import sys

# Read the input from stdin
commands = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

# Call the function to calculate the maximum distance
max_dist = max_distance(commands, n)

# Print the result to stdout
print(max_dist)
