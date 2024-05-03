import sys

n = int(sys.stdin.readline().strip())  # number of commands that can be modified
commands = list(map(str.strip, sys.stdin.readlines()))  # list of turtle commands

max_distance = 0
current_position = 0

for command in commands:
    if command == 'F':
        current_position += 1
        max_distance = max(max_distance, current_position)
    elif command == 'T':
        # turn around, reset position
        current_position = 0

print(max_distance)

dp = [[0] * (n + 1) for _ in range(len(commands) + 1)]

for i in range(1, len(commands) + 1):
    for j in range(min(i, n) + 1):
        if commands[i - 1] == 'F':
            dp[i][j] = max(dp[i - 1][j], current_position)
        elif commands[i - 1] == 'T':
            # turn around, reset position
            dp[i][j] = 0

print(max(max(row) for row in dp))
