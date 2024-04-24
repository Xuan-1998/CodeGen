def generate_fibonacci(n):
    # The first two Fibonacci numbers
    fib = [1, 1]
    
    # Generate the next n-2 Fibonacci numbers
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return fib

# Read the input from stdin
N = int(input().strip())

# Generate the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(N)

# Print the result to stdout
print(' '.join(map(str, fibonacci_numbers)))
