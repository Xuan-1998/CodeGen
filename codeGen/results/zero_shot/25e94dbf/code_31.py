def max_distance(commands, n):
    # Initialize the current position and distance traveled
    x, y = 0, 0
    distance = 0

    for command in commands:
        if command == "F":
            x += 1
            distance += 1
        elif command == "T":
            # Turn around: move back to the starting point
            x -= 2 * (x - y)
            y = x
            distance += abs(x) + abs(y)

    # Modify at most n commands to maximize the distance traveled
    for _ in range(n):
        max_dist = 0
        best_command_idx = None

        for i, command in enumerate(commands):
            if command == "F":
                new_distance = x + 1
                if new_distance > max_dist:
                    max_dist = new_distance
                    best_command_idx = i
            elif command == "T":
                # Turn around: move back to the starting point
                new_x = x - abs(x)
                new_y = y
                new_distance = abs(new_x) + abs(new_y)
                if new_distance > max_dist:
                    max_dist = new_distance
                    best_command_idx = i

        if best_command_idx is not None:
            commands[best_command_idx] = "F"  # or turn around, depending on the choice

    return distance
