import sys
import random

n, commands = int(sys.stdin.readline()), list(sys.stdin.readline().strip())
pos_x, pos_y = 0, 0
dir = 0

for cmd in commands:
    if cmd == 'F':
        if dir == 0:  # North
            pos_y += 1
        elif dir == 1:  # East
            pos_x += 1
        elif dir == 2:  # South
            pos_y -= 1
        else:  # West
            pos_x -= 1
    else:  # Turn around (T)
        if dir == 0:  # North
            dir = 3  # West
        elif dir == 1:  # East
            dir = 2  # South
        elif dir == 2:  # South
            dir = 1  # East
        else:  # West
            dir = 0  # North

max_dist = 0

for _ in range(n):
    idx = int(random.random() * len(commands))
    if commands[idx] == 'F':
        # Turn around (T) at this position
        if dir == 0:  # North
            dir = 3  # West
        elif dir == 1:  # East
            dir = 2  # South
        elif dir == 2:  # South
            dir = 1  # East
        else:  # West
            dir = 0  # North
    else:  # Turn around (T) at this position
        if dir == 0:  # North
            dir = 3  # West
        elif dir == 1:  # East
            dir = 2  # South
        elif dir == 2:  # South
            dir = 1  # East
        else:  # West
            dir = 0  # North

    # Simulate the modified command
    commands[idx] = 'F' if random.random() > 0.5 else 'T'
    for cmd in commands:
        if cmd == 'F':
            if dir == 0:  # North
                pos_y += 1
            elif dir == 1:  # East
                pos_x += 1
            elif dir == 2:  # South
                pos_y -= 1
            else:  # West
                pos_x -= 1
        else:  # Turn around (T)
            if dir == 0:  # North
                dir = 3  # West
            elif dir == 1:  # East
                dir = 2  # South
            elif dir == 2:  # South
                dir = 1  # East
            else:  # West
                dir = 0  # North

    max_dist = max(max_dist, abs(pos_x) + abs(pos_y))

print(max_dist)
