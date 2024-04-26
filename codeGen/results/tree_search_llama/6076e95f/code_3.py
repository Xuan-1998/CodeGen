def generate_sequence():
    # Read input from stdin
    start, end = map(int, input().split())

    # Create a list of ranges
    ranges = [(start, end)]

    # Initialize the sequence and current range
    sequence = []
    current_range = ranges[0]

    # Generate the sequence
    i = current_range[0]
    while i <= current_range[1]:
        sequence.append(i)
        i += 1

    # Print the sequence to stdout
    print(*sequence, sep='\n')

# Call the function
generate_sequence()
