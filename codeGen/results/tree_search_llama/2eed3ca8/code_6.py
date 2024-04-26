def is_circular_sequence(sequence):
    start_pos = 0
    for move in sequence:
        if move == "forward":
            start_pos += 1
        elif move == "left" or move == "right":
            pass
    return start_pos == 0

sequence = input()
print("Circular" if is_circular_sequence(sequence) else "Not Circular")
