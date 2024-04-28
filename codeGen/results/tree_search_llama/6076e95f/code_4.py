def generate_sequence():
    # Read input from stdin
    start, end = map(int, input().split())

    # Use the range function to generate the sequence
    sequence = list(range(start, end + 1))

    # Print the sequence to stdout
    print(sequence)

if __name__ == "__main__":
    generate_sequence()
