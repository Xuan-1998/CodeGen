def generate_fibonacci(n):
    # Base cases
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize the first two Fibonacci numbers
    fib_sequence = [1, 1]
    
    # Generate the Fibonacci sequence up to the Nth number
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Read the input from stdin
N = int(input().strip())

# Generate and print the Fibonacci sequence
fibonacci_numbers = generate_fibonacci(N)
for number in fibonacci_numbers:
    print(number, end=' ')
print()  # For a new line at the end
