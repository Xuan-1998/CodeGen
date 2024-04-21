def generate_fibonacci(n):
    if n == 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]  # Sum the last two numbers
        fib.append(next_fib)  # Append the result to the list
    return fib

# Receive input from stdin
n = int(input())

# Generate and print the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(n)
print(fibonacci_numbers)
