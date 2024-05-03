def simulate_turtle(commands):
    current_position = 0
    direction = 1  # 1 for moving forward, -1 for moving backward

    for command in commands:
        if command == "F":
            current_position += direction
        elif command == "T":
            direction *= -1

    return current_position

def modify_commands(commands, n):
    modified_commands = list(commands)  # create a copy of the original commands

    for i in range(n):
        if modified_commands[i] == "T":
            modified_commands[i] = "F"

    return modified_commands

def find_max_distance(modified_commands, n):
    max_distance = 0

    for i in range(n):
        modified_commands = modify_commands(modified_commands, i)
        current_position = simulate_turtle(modified_commands)
        max_distance = max(max_distance, current_position)

    return max_distance

def main():
    commands = input().split()
    n = int(input())
    modified_commands = modify_commands(commands, n)
    max_distance = find_max_distance(modified_commands, n)

    print(max_distance)

if __name__ == "__main__":
    main()
