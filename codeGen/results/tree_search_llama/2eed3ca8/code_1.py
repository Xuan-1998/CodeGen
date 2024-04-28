def circular_sequence():
    # Initialize an empty dictionary
    positions = {}

    # Read the sequence of moves from standard input
    sequence = input().strip()

    # Iterate through the sequence, updating the position and storing it in the dictionary
    for move in sequence:
        if move == 'F':  # Forward movement
            positions[positions.get('pos', 0) + 1] = 'F'
        elif move == 'L' or move == 'R':
            # For simplicity, assume left/right turns don't change the position
            pass

    # Check if the initial position is present in the dictionary (assuming it's position 0)
    if 0 in positions:
        return "Circular"
    else:
        return "Not Circular"

print(circular_sequence())
