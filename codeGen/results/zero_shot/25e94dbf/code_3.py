import sys

def maximize_distance(commands, n):
    total_distance = 0
    current_direction = 1 if commands[0] == 'F' else 0
    modified_commands = set()

    for i, command in enumerate(commands):
        if command == 'F':
            total_distance += 1
            if current_direction == 0:
                current_direction = 1
            else:
                current_direction = 0
        elif command == 'T' and n > 0:
            # modify the command by either turning around or moving forward
            if i not in modified_commands:
                if random.choice([True, False]):
                    commands[i] = 'F'
                else:
                    commands[i] = 'T'
                modified_commands.add(i)
                n -= 1

    return total_distance

if __name__ == '__main__':
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    print(maximize_distance(commands, n))
