def generate_fibonacci(n):
    if n == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

# Read input from stdin
n = int(input().strip())

# Generate the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)

# Print the Fibonacci numbers to stdout
print(fibonacci_numbers)
