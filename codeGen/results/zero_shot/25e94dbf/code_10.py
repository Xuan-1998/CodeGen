def max_distance(commands, n):
    # Calculate the total distance traveled by summing up all "F" commands
    total_distance = 0
    for command in commands:
        if command == 'F':
            total_distance += 1

    # Apply transformations to increase the distance traveled (at most n/2 times)
    while n > 0 and total_distance % 2 == 0:  # check if we can apply the transformation
        n -= 1
        total_distance += 1  # add one "F" command
        commands = 'F' + commands[:-1]  # update the list of commands

    return total_distance

# Example usage:
commands = input()  # read the string of commands from stdin
n = int(input())  # read the number of modifications available from stdin
print(max_distance(commands, n))  # print the maximum distance traveled to stdout
