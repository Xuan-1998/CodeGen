def is_circular(moves):
    x, y = 0, 0  # Initial position (0, 0)
    directions = {'F': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # Forward, Left, Right

    for move in moves:
        dx, dy = directions[move]
        x += dx
        y += dy

    if (x, y) == (0, 0):  # If the final position is the same as the initial position
        return "Circular"
    else:
        return "Not Circular"

moves = input().strip()
print(is_circular(moves))
