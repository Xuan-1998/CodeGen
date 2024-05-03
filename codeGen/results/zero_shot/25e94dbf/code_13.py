import sys
import itertools

commands = []
for command in sys.stdin.readline().strip():
    commands.append(command)

n = int(sys.stdin.readline())

def distance(commands):
    x, y = 0, 0
    for command in commands:
        if command == "F":
            y += 1
        elif command == "T":
            x, y = -x, -y
    return abs(x) + abs(y)

def optimize_commands(commands):
    for combination in itertools.combinations(commands, n):
        distance_val = distance(list(combination))
        if distance_val > max_distance:
            max_distance = distance_val
    return max_distance

max_distance = 0
print(optimize_commands(commands))
