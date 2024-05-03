# Step 1: Define the input variables
commands = input().strip()  # Read the commands string from stdin
n = int(input())  # Read the number of commands that can be modified from stdin

# Step 2: Initialize a dictionary to store the distances for each command
distances = {"T": 0, "F": 1}

# Step 3: Calculate the total distance traveled by the turtle for the given commands
total_distance = 0
for command in commands:
    if command == "T":
        if total_distance % 2 == 0:
            total_distance += 2
        else:
            total_distance -= 2
    elif command == "F":
        total_distance += distances[command]

# Step 4: Modify the commands to maximize the distance traveled by the turtle
modified_commands = list(commands)
for i in range(n):
    if modified_commands[i] == "T" and total_distance % 2 != 0:
        modified_commands[i] = "F"
    elif modified_commands[i] == "F":
        if total_distance + distances["T"] - distances["F"] > total_distance:
            modified_commands[i] = "T"

# Step 5: Calculate the maximum distance traveled by the turtle for the modified commands
modified_total_distance = 0
for command in modified_commands:
    if command == "T":
        if modified_total_distance % 2 == 0:
            modified_total_distance += 2
        else:
            modified_total_distance -= 2
    elif command == "F":
        modified_total_distance += distances[command]

# Step 6: Print the maximum distance traveled by the turtle
print(modified_total_distance)
