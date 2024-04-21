# Receive input from stdin
N = int(input())

def calculate_fibonacci(N):
    # Check if N is 1 or 2 and handle those cases
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    
    # Initialize the list with the first two Fibonacci numbers
    fib = [1, 1]
    
    # Calculate the next Fibonacci numbers and append to the list
    for i in range(2, N):
        next_fib = fib[-1] + fib[-2]  # Sum the last two elements
        fib.append(next_fib)
    
    return fib

# Calculate the first N Fibonacci numbers
fibonacci_numbers = calculate_fibonacci(N)

# Print the result to stdout
print(fibonacci_numbers)
