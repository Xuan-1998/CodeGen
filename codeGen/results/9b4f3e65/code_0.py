def generate_fibonacci(N):
    # The first two Fibonacci numbers
    fib = [1, 1]
    
    # Generate the remaining Fibonacci numbers up to N
    for i in range(2, N):
        fib.append(fib[-1] + fib[-2])
    
    return fib

# Read input from stdin
N = int(input().strip())

# Check if N is 1, we only need the first Fibonacci number
if N == 1:
    print([1])
else:
    # Generate and print the first N Fibonacci numbers
    fibonacci_numbers = generate_fibonacci(N)
    print(fibonacci_numbers)
