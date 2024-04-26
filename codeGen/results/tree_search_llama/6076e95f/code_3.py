def generate_sequence():
    start = int(input("Enter the starting integer: "))
    end = int(input("Enter the ending integer: "))

    # Generate the sequence
    sequence = list(range(start, end + 1))

    return sequence

sequence = generate_sequence()
print(sequence)
