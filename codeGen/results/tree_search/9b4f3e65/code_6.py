def generate_fibonacci(n):
    # Initialize the list with the first two Fibonacci numbers
    fib = [1, 1]
    
    # If the user wants only the first Fibonacci number
    if n == 1:
        return [1]
    
    # Iterate from 2 to N-1 (inclusive) to generate the next Fibonacci numbers
    for i in range(2, n):
        # Append the sum of the last two numbers in the list to the list itself
        fib.append(fib[-1] + fib[-2])
    
    # Return the list of the first N Fibonacci numbers
    return fib

# Read the input from standard input
N = int(input().strip())

# Generate the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(N)

# Print the list of Fibonacci numbers to standard output
print(fibonacci_numbers)
