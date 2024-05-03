def max_distance(commands, n):
    # Initialize the current position and direction
    x, y = 0, 0
    dx, dy = 1, 0

    for i in range(len(commands)):
        if commands[i] == "T":
            # Turn around
            dx, dy = -dx, -dy
        elif commands[i] == "F":
            # Move forward
            x += dx
            y += dy

        # Modify at most n commands
        for j in range(min(n, i+1)):
            if random.random() < 0.5:
                # Turn around with 50% chance
                dx, dy = -dx, -dy
            elif random.random() < 0.75:
                # Move forward with 25% chance
                x += dx
                y += dy

    return abs(x) + abs(y)

# Example usage
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
