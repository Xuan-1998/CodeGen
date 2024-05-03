def max_turtle_distance(commands, n):
    max_distance = 0
    current_position = 0

    for command in commands:
        if command == "F":
            current_position += 1
        elif command == "T" and n > 0:
            command = "F"
            n -= 1

    max_distance = abs(current_position)

    return max_distance

# Example usage:
commands = input()  # Read the commands from stdin
n = int(input())  # Read the number of modifications allowed

print(max_turtle_distance(commands, n))  # Output the maximum distance
