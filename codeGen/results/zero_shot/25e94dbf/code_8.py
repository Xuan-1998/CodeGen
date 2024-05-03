import sys

def max_distance(commands, n):
    distance = 0
    for i, cmd in enumerate(commands):
        if cmd == "F":
            distance += 1
        elif cmd == "T" and i < len(commands) - n:
            # Replace with an "F" command
            commands[i] = "F"
    return distance

commands = input().strip()
n = int(input())
print(max_distance(commands, n))
