def check_circular_sequence():
    moves = input().strip()

    if len(moves) == 0:
        return "Not Circular"

    start_position = {'F': 1, 'L': -1, 'R': 1}.get(moves[0])

    end_position = 0

    for move in moves:
        position_change = {'F': 1, 'L': -1, 'R': 1}.get(move)
        end_position += position_change

        if end_position < 0:
            return "Not Circular"

    return "Circular" if start_position == end_position else "Not Circular"

print(check_circular_sequence())
