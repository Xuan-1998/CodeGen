def calculate_circularity(moves):
    # Initialize variables to keep track of the robot's position and direction
    x, y, dx, dy = 0, 0, 1, 0

    for move in moves:
        if move == "F":
            # Move forward
            x += dx
            y += dy
        elif move == "L":
            # Turn left
            dx, dy = -dy, dx
        elif move == "R":
            # Turn right
            dx, dy = dy, -dx

    # Check if the robot ended up back at its starting position
    if (x, y) == (0, 0):
        return "Circular"
    else:
        return "Not Circular"
