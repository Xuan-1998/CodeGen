def generate_sequence():
    # Receive inputs from stdin
    start, end = map(int, input().split())
    
    # Initialize an empty list
    sequence = []
    
    # Populate the list with the integers in the desired range
    for i in range(start, end + 1):
        sequence.append(i)
    
    # Print the output to stdout
    print(*sequence)

# Call the function to execute it
generate_sequence()
