def generate_sequence():
    start, end = map(int, input("Enter the first integer: ").split())
    sequence = list(range(start, end + 1))
    print(sequence)

generate_sequence()
