def generate_sequence():
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))

    # Make sure the end value is greater than or equal to the start value
    if start > end:
        print("Invalid input! The start value should be less than or equal to the end value.")
        return

    sequence = list(range(start, end + 1))  # Note the 'end + 1'
    print(sequence)

generate_sequence()
