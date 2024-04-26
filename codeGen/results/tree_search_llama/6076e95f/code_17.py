def generate_integer_sequence():
    start_value = int(input("Enter the starting integer: "))
    end_value = int(input("Enter the ending integer: "))

    if start_value > end_value:
        print("Invalid input. The starting value should be less than or equal to the ending value.")
        return

    sequence = list(range(start_value, end_value + 1))
    print(sequence)

generate_integer_sequence()
