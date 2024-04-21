def fibonacci(n):
    # Base case: if n is 1 or 2, return the list with first n Fibonacci numbers
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    # Initialize the list with the first two Fibonacci numbers
    fib = [1, 1]
    
    # Calculate the remaining Fibonacci numbers iteratively
    for i in range(2, n):
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)
    
    return fib

# Read input from stdin
n = int(input())

# Generate the first N Fibonacci numbers
fibonacci_numbers = fibonacci(n)

# Print the result to stdout
print(fibonacci_numbers)
