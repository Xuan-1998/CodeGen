def generate_sequence():
    first_integer = int(input("Enter the first integer: "))
    second_integer = int(input("Enter the second integer: "))

    sequence = []

    current_integer = first_integer

    while current_integer <= second_integer:
        sequence.append(current_integer)
        current_integer += 1

    return sequence

sequence = generate_sequence()

print(sequence)
