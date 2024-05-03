input_string = input()  # read input string from stdin
n = int(input())  # read integer n from stdin

current_direction = 0
max_distance = 0

for command in input_string:
    if command == "F":
        if current_direction == 0:  # north
            max_distance += 1
        elif current_direction == 1:  # east
            max_distance += 1
        elif current_direction == 2:  # south
            max_distance -= 1
        elif current_direction == 3:  # west
            max_distance -= 1

        if current_direction == 0 or current_direction == 2:
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4
    elif command == "T":
        current_direction = (current_direction + 2) % 4

for _ in range(n):
    pass  # implement modification logic here

print(max_distance)
