import random

commands = input()  # receive the string of turtle commands
n = int(input())  # receive the number of commands that can be modified

distance = 0
for command in commands:
    if command == "F":
        distance += 1
    elif command == "T":
        distance = 0

# modify exactly n commands
modified_commands = list(commands)
random.shuffle(modified_commands[:n])
for i in range(n):
    if modified_commands[i] == "F":
        modified_commands[i] = "T"
    else:
        modified_commands[i] = "F"

print(distance)  # print the maximum distance traveled by the turtle
