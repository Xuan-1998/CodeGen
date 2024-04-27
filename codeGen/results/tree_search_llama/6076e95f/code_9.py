def generate_sequence():
    first_integer = int(input("Enter the first integer: "))
    second_integer = int(input("Enter the second integer: "))

    sequence = []
    for i in range(first_integer, second_integer + 1):
        sequence.append(i)

    return sequence

print(generate_sequence())
