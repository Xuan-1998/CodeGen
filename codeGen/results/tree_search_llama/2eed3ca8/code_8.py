def is_circular(input_string):
    # Define a dictionary to map directions
    directions = {'R': 1, 'L': -1}

    current_position = (0, 0)  # Initialize the robot's position
    current_direction = 0  # Initialize the robot's direction

    for move in input_string:
        if move in directions:  # If the move is a change in direction
            current_direction *= -1  # Change the direction accordingly
        else:  # If the move is forward
            current_position = (current_position[0] + current_direction, current_position[1])
            if current_position == (0, 0):  # If we're back at the starting position
                return "Circular"

    return "Not Circular"  # If we didn't end up back at the starting position


def main():
    input_string = input()
    print(is_circular(input_string))


if __name__ == "__main__":
    main()

