def solution():
    n = int(input())  # Read input from stdin

    count = 0  # Initialize counter
    for i in range(n + 1):
        if no_consecutive_ones(i):  # Check if binary representation does not contain consecutive ones
            count += 1  # Increment counter if condition met

    print(count)  # Print the result to stdout

solution()
