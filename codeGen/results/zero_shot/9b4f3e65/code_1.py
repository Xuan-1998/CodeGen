def generate_fibonacci(n):
    # Base cases for n = 1 and n = 2
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    # Start the list with the first two Fibonacci numbers
    fib_sequence = [1, 1]
    
    # Calculate the rest of the Fibonacci sequence
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Read the input from standard input
n = int(input().strip())

# Generate the Fibonacci sequence
fib_sequence = generate_fibonacci(n)

# Print the sequence to standard output
print(' '.join(map(str, fib_sequence)))
