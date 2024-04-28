from collections import deque

def is_circular_move_sequence(move_sequence):
    move_map = {'F': 1, 'L': -1, 'R': 1}
    position_queue = deque([(0, 0)])  # (position, direction)
    last_position = None

    for move in move_sequence:
        if move == 'F':
            new_position = position_queue[-1][0] + move_map[move]
            position_queue.append((new_position, position_queue[-1][1]))
        elif move == 'L' or move == 'R':
            direction = -1 if move == 'L' else 1
            position_queue.append((position_queue[-1][0], position_queue[-1][1] * direction))

        last_position = new_position

    return last_position == position_queue[0][0]

move_sequence = input()

if is_circular_move_sequence(move_sequence):
    print("Circular")
else:
    print("Not Circular")
