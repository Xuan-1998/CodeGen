import sys

commands = input().strip()
n = int(input())

current_position = [0, 0]  
distance_traveled = 0
best_distance = 0

def move_turtle(command):
    global current_position, distance_traveled, best_distance

    if command == "F":
        current_position[1] += 1
        distance_traveled += 1
        best_distance = max(best_distance, distance_traveled)
    elif command == "T":
        current_position = [-current_position[0], current_position[1]]

for i in range(len(commands)):
    if i < n:
        # modify the command here (e.g., replace "T" with "F")
        pass  # TO DO: implement the modification logic

    move_turtle(commands[i])

print(best_distance)
