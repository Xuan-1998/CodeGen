# Receive the input commands and the number of modifications allowed
commands = input().strip()
n = int(input())

# Initialize the maximum distance to 0
max_distance = 0

# Define a function to calculate the distance for a given sequence of commands
def calculate_distance(commands):
    direction = 'right'
    distance = 0
    
    for command in commands:
        if command == 'F':
            if direction == 'right':
                distance += 1
            elif direction == 'left':
                distance -= 1
        elif command == 'T':
            if direction == 'right':
                direction = 'left'
            else:
                direction = 'right'
    
    return distance

# Initialize the best possible sequence of commands with the given sequence
best_commands = list(commands)

# Define a function to modify the sequence of commands and calculate the resulting distance
def try_modification(best_commands, n):
    for i in range(n):
        if best_commands[i] == 'F':
            best_commands[i] = 'T'
            yield best_commands
            best_commands[i] = 'F'
        else:
            yield best_commands
            best_commands[i] = 'F'
    yield best_commands

# Try all possible modifications and keep track of the maximum distance
for modified_commands in try_modification(best_commands, n):
    max_distance = max(max_distance, calculate_distance(modified_commands))

print(max_distance)
