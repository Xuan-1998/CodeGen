def is_circular(moves):
    initial_position = 0
    for move in moves:
        if move == 'F':
            initial_position += 1
        elif move == 'L':
            initial_position = (initial_position - 1) % 3
        elif move == 'R':
            initial_position = (initial_position + 1) % 3
    return initial_position == 0

moves = input()
print("Circular" if is_circular(moves.split()) else "Not Circular")
