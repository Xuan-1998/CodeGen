def generate_arithmetic_progression():
    # Read input integers from stdin
    first_integer = int(input())
    last_integer = int(input())

    # Generate the arithmetic progression using a list comprehension
    sequence = [first_integer + i for i in range(last_integer - first_integer + 1)]

    # Print the generated sequence to stdout
    print(sequence)

# Call the function to generate and print the sequence
generate_arithmetic_progression()
