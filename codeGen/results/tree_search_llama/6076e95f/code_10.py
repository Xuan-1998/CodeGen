def generate_sequence():
    # Read input integers from stdin
    a, b = map(int, input().split())

    # Initialize an empty list to store the sequence
    seq = []

    # Loop until the current value is greater than or equal to b
    for i in range(a, b + 1):
        seq.append(i)

    # Print the generated sequence to stdout
    print(" ".join(map(str, seq)))

# Call the function
generate_sequence()
